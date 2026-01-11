---
layout: post
title: "Passing Parameters."
subtitle: "Calling Conventions and LEA instruction."
date: 2025-12-04 09:00:00 +0000
categories: ['Past Blogs', 'Assembly']
tags: ['x86', 'reverse-engineering']
author: German Sanmi
---


### 1. Parameter Definition.

First, a *parameter* is simply data that gets placed in a specific location where the calling convention dictates the callee should look for it. This means that is data that a called function knows where to find it.

Consider the following code:

```c
int func(int a){
	int i = a;
	return i;
}
int main(){
	return func(0x11);
}
```

The func() function accepts a parameter which is defined in the signature as a signed integer. 

Let's get the dissasembly, this is achieve through :

```assem
0x00001129      f30f1efa       endbr64    ;  Intel CET instruction
0x0000112d      55             push rbp
0x0000112e      4889e5         mov rbp, rsp
0x00001131      897dec         mov dword [rbp - 0x14], edi ; arg1
0x00001134      8b45ec         mov eax, dword [rbp - 0x14]
0x00001137      8945fc         mov dword [rbp - 4], eax
0x0000113a      8b45fc         mov eax, dword [rbp - 4]
0x0000113d      5d             pop rbp
0x0000113e      c3             ret

int main (int argc, char **argv, char **envp);
0x0000113f      f30f1efa       endbr64
0x00001143      55             push rbp
0x00001144      4889e5         mov rbp, rsp
0x00001147      bf11000000     mov edi, 0x11               ; int64_t arg1
0x0000114c      e8d8ffffff     call sym.func
0x00001151      5d             pop rbp
0x00001152      c3             ret
```

- First, the return address:

    ```
    0x0000112d      55             push rbp
    0x0000112e      4889e5         mov rbp, rsp
    ```

- Then, the parameter, main calls *func()* passing the hex value *0x11*. Since this is a Linux system (compiled with GCC in WSL) the parameter gets stored in RDI, then calls the function:

    ```assem
    0x00001147      bf11000000     mov edi, 0x11
    0x0000114c      e8d8ffffff     call sym.func
    ```

    This is a convention, according to our definition of a parameter, 0x11 is a value that, for convention, func knows where to find (in RDI).

- The flow of execution enters func() which assigns this parameter to a local variable for which resorts EDI:

    ```assem
    0x0000112d      55             push rbp
    0x0000112e      4889e5         mov rbp, rsp
    0x00001131      897dec         mov dword [rbp - 0x14], edi ; arg1
    ```

    Then returns the value by passing this following value to EAX in a convoluted way:

    ```assem
    0x00001134      8b45ec         mov eax, dword [rbp - 0x14]
    0x00001137      8945fc         mov dword [rbp - 4], eax
    0x0000113a      8b45fc         mov eax, dword [rbp - 4]
    ```

<br>

### 2. x64. Calling Conventions.

Assembly doesn't have a built-in concept of "functions" like high-level languages do. Instead, it uses calling conventions; standardized rules for how to pass arguments and manage the stack when calling subroutines.

There are two main frameworks by platform:

**Windows x64 (Microsoft x64 ABI)**

- First 4 arguments: Passed in registers RCX, RDX, R8, R9 (in that order)
- Additional arguments: Passed on the stack (right-to-left)
- Floating-point arguments: Use XMM0, XMM1, XMM2, XMM3
- Return value: RAX (RDX:RAX) for integers, XMM0 for floats
- A compiler example is MCVS 2019.

Consider the main's code compiled in MCVS 2019:

```
0000000140001020 48 83 EC 28          sub         rsp,28h  
0000000140001024 B9 11 00 00 00       mov         ecx,11h  <--- ECX (RCX) to store 0x11
0000000140001029 E8 D2 FF FF FF       call        func (0140001000h)  
000000014000102E 48 83 C4 28          add         rsp,28h  
0000000140001032 C3                   ret 
```

<br>

**System V AMD64 ABI (Linux, macOS)**

- First 6 integer arguments: RDI, RSI, RDX, RCX, R8, R9
- First 8 float arguments: XMM0 through XMM7
- Additional arguments: Passed on the stack
- Return value: RAX (RDX:RAX) for integers, XMM0 for floats
- A compiler example is GCC.

<br>

In general:

- Both caller and callee are responsible for balancing any register saves they perform (add to the stack), with restores (removal from the stack). Caller will typically save registers right before the call and restore right after the call and the callee will typically save registers at the beginning of the function and restore at the end of the function.

<br>

### 3. Shadow Store.

Shadow store (also called home space or shadow space) is a Windows x64-specific feature by which the caller must allocate 32 bytes (4 × 8-byte slots) on the stack before calling a function, the space corresponds to 4 register-passed parameters. Then, the callee can optionally use this space to "spill" (save) those register values if needed.

Is like a sort of a caller's "inverse"-stackframe for register-passed parameter to the callee exclusive of Microsoft x64 ABI calling-convention programs.

The term 'inverse' refers to the fact that the shadow space is created first before the CALL of the callee in terms of instruction execution order and also is above his own stackframe (if it exists). 

This is, if a caller reserve a shadow space for a callee, then the callee access this space by going up in the stack (towards higher address), accessing the stack-context of the caller function (rbp+0x08), the stackframe would be created after the callee is invoked and everytime the callee wants to access his own stackframe he must go below the calleer in terms of stackdiagram (rbp-0x08)

<br>

```
┌─────────────────────────┐  Higher addresses
│                         │
│  Shadow space           │  ← Callee accesses via [rsp+8], [rsp+10], etc.
│  (caller allocated)     │     Going UP (positive offsets)
│                         │
├─────────────────────────┤  ← Return address pushed by CALL
│  return addr            │
├─────────────────────────┤  ← rsp after CALL, before callee prologue
│                         │
│  Callee's own frame     │  ← Callee accesses via [rsp-8] or [rbp-8]
│  (locals, saved regs)   │     Going DOWN (negative offsets)
│                         │
└─────────────────────────┘  Lower addresses
```

<br>

### 4. Instruction LEA. Load Effective Address.

Consider the following C code:

```c
int main(int argc, char** argv) {
    int a;
    //reminder: atoi() converts an
    //ASCII string to an integer
    a = atoi(argv[1]);
    return 2 * argc + a;
}
```

This code declares a variable and then assigns to it a value passed by a command line argument and processed by *atoi()* (ASCII to Integer), which yields an integer from a provided string.

Then returns 2 times the number of argumets passed through the command line to the program plus 'a'.

<br>

Then, we have the following dissasembly through MCVS 2019:

```assem
0000000140001000 40 53                push        rbx  
0000000140001002 48 83 EC 20          sub         rsp,20h  
0000000140001006 8B D9                mov         ebx,ecx  
0000000140001008 48 8B 4A 08          mov         rcx,qword ptr [rdx+8]  
000000014000100C FF 15 66 31 00 00    call        qword ptr [__imp_atoi (0140004178h)]  
0000000140001012 8D 04 58             lea         eax,[rax+rbx*2]  
0000000140001015 48 83 C4 20          add         rsp,20h  
0000000140001019 5B                   pop         rbx  
```

Is worth to note before enter to explain LEA, that the code above is importing dynamically atoi() function from \<stdlib.h\> and because of that is trying to access to atoi() by dereferencing an external address through '_imp' directive.

Also, we could think that 

```asssem
0000000140001002 48 83 EC 20          sub         rsp,20h  
```

Is the prologue to the stackframe, buit is not. Since a callee is about to be called by the main function (and this program follows MC x64 ABI calling-conventions) a shadow space for register-passed parameters needs to be allocated.

The key to distinguish between is by context, if you look closer to the code: 

- First, there is no need from stackframe since there is only one local variable (which also is never stored somepoint behind rbx) 

- There is a callee and this is MC x64 ABI program so the rsp substraction needs to be the shadow space allocation

<br>

Lets talk about LEA.

Often, in assembly the brackets [] is a directive which tells the system to dereference which is inside as a memory address, but is not the case with LEA. 

With LEA an arithmeticv operation is gonna be pass to between brackets. LEA would solve that operation and then store that value in a register.

For example, in our code there is the line:

```
0000000140001012 8D 04 58             lea         eax,[rax+rbx*2] 
```

Which simply calculates "rax+rbx*2" and store that value on EAX.

So it just moves the value within the brackets (it resolves an operation if proceeds) int

<br>

