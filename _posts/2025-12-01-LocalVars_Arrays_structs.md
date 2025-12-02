---
layout: post
title: Stackframe: Local variables, Arrays and Structures.
subtitle: Assembly management of local variables, arrays and structures.
tags: [assem]
---

### 1. Defintion.

Let's consider the following code:

```c
int calculate(int a, int b) {
    int result;
    int temp = 5;
    result = a + b + temp;
    return result;
}

int main() {
    int x = calculate(10, 20);
    return x;
}
```

We have a C code which returns a calculated value using a local function, *calculate()* which receives two parameters as data and then use their own local variables to calculate and return the value (temp, result).

So let's begin from the start. **Local variables** are temporary storage locations used within a function's scope. Unlike global variables stored in the DATA segment, local variables are allocated on the stack and automatically destroyed when the function returns. Examples of local variables in the code above are *result* declared an later assigned or *temp* directly defined both within *calculate()* function.

<br>

### 2. Local variales in assembly.

Let's see how local variables are treated in assembly. We know that there is a structure called the stack in which things like local variables are pushed as part of the context of called function. The own system expands the stack in order to allocate in a sort order the elements that the function needs to properly works along with other things (saved registers, parameters and the return address), this expansion is what we call the *function's stackframe*.

The traslation to assembly of the code above would be:

```assem
calculate:
0000000140001000 push   rbp
0000000140001001 mov    rbp, rsp
0000000140001004 sub    rsp, 10h
0000000140001008 mov    DWORD PTR [rbp-4], ecx      ; parameter a
000000014000100B mov    DWORD PTR [rbp-8], edx      ; parameter b
000000014000100E mov    DWORD PTR [rbp-0Ch], 5      ; temp = 5
0000000140001015 mov    eax, DWORD PTR [rbp-4]      ; load a
0000000140001018 add    eax, DWORD PTR [rbp-8]      ; add b
000000014000101B add    eax, DWORD PTR [rbp-0Ch]    ; add temp
000000014000101E mov    DWORD PTR [rbp-10h], eax    ; result = ...
0000000140001021 mov    eax, DWORD PTR [rbp-10h]    ; return result
0000000140001024 add    rsp, 10h
0000000140001028 pop    rbp
0000000140001029 ret

main:
0000000140001030 push   rbp
0000000140001031 mov    rbp, rsp
0000000140001034 sub    rsp, 20h
0000000140001038 mov    ecx, 0Ah                    ; first argument: 10
000000014000103D mov    edx, 14h                    ; second argument: 20
0000000140001042 call   calculate (0140001000h)
0000000140001047 mov    DWORD PTR [rbp-4], eax      ; x = result
000000014000104A mov    eax, DWORD PTR [rbp-4]      ; return x
000000014000104D add    rsp, 20h
0000000140001051 pop    rbp
0000000140001052 ret
```

Where the RPI would contain the address 0000000140001030 at the start of the program (the main's address).

<br>

### 3. Stack Frame Creation.

#### 3.1. Brief warning.

Is worth mention that the creation of a stack frame using RBP is an optional procedure that's primarily a compiler convention rather than a hardware requirement in oposition like for example RIP manipulation by CALL/RET. 


Note that despite CALL/RET perform operations over RIP, this is a hardware requirement and is done automatically by the CPU, you will never see reflected in the code the lines:

```assem
push RIP + jmp target (CALL)
pop RIP + jmp RIP (RET)
```

But, instead we will see how RSP and RBP special-purpouse pointers get manipulated allong the following procedure. This is done for easier debugging, simpler code generation o dynamic stack allocation.

<br>

#### 3.2. Process explanation.

##### 3.2.1. Stackframe Creation Prologue.

First, lets see how the stackframe for the local function is created.

The code starts executing main function which is at: 0000000140001030, then the execution flow continues until *calculate()* is called. Then, the CALL instruction intervenes pushing 0000000140001047 onto the top of the stack and then introduces on RIP register the calculate function's address: 0000000140001000. (Remember that RIP contains the address of the next instruction to be executed, it basically controls the execution flows of the code)

Once the execution flow enters *calculate()* as a local function the creation of his stackframe in the stack begins:

```assem
0000000140001000 push   rbp
0000000140001001 mov    rbp, rsp
0000000140001004 sub    rsp, 10h
```

Let's check carefully the register within the code above:

- RBP -> Base Pointer, points to the base of the current stackframe. Serves as a stable reference point for accessing local variables and parameters.

- RSP -> Stack Pointer, points to the top of the stack.

So, first, we save the current RBP (the address of the current stackframe) pushing it on the stack and place a new *base stackframe* by copying the current RSP value (the lowest address pushed on the stack) onto RBP. Lastly, we lowered the RSP value in order to build a secure margin to the function context. Essentially, since the stack grows toward lower address and RSP points to the top of the stack, substracting RSP we are expanding the stack (this, despite being counter-intuitive, is neccesary due to processor's execution patterns and the compiler's code generation needs).

```assem

High Memory (Stack grows downward ↓)

┌─────────────────────────────────────────┐
│                  ...                    │
├─────────────────────────────────────────┤
│  Return address to main                 │  Pushed by CALL
├─────────────────────────────────────────┤ ← RSP before prologue
│  Saved RBP (old frame pointer)          │  Pushed by: push rbp
├─────────────────────────────────────────┤ ← RBP (current frame base)
│  [rbp-4]:  parameter a (10)             │
├─────────────────────────────────────────┤
│  [rbp-8]:  parameter b (20)             │
├─────────────────────────────────────────┤
│  [rbp-0Ch]: temp (5)                    │
├─────────────────────────────────────────┤
│  [rbp-10h]: result (35)                 │
├─────────────────────────────────────────┤ ← RSP (current stack top)
│                  ...                    │

Low Memory
```

Note that local variables as well as paramters are accesed using "r/mX" notation.

<br>

##### 3.2.2. Accessing local variables and Stackframe epilogue.

Now that a stackframe has being created, then the local variables and parameters of the function are alocated within this stackframe.

Those are accessed using the RBP base pointer plus an offset. Let's check that:

```asem
0000000140001008 mov    DWORD PTR [rbp-4], ecx      ; parameter a
000000014000100B mov    DWORD PTR [rbp-8], edx      ; parameter b
000000014000100E mov    DWORD PTR [rbp-0Ch], 5      ; temp = 5
0000000140001015 mov    eax, DWORD PTR [rbp-4]      ; load a
0000000140001018 add    eax, DWORD PTR [rbp-8]      ; add b
000000014000101B add    eax, DWORD PTR [rbp-0Ch]    ; add temp
```

First, the parameters of the function which by default are in RCX, RDX, R8, R9 gets stored inside te stackframe:

```assem
0000000140001008 mov    DWORD PTR [rbp-4], ecx      ; parameter a
000000014000100B mov    DWORD PTR [rbp-8], edx      ; parameter b
```

Note that we are copying the contents of ECX (RCX variant in 32-bits) into a memory region behind RBP, the DWORD PTR term is used to refer that \[rbp-4\] is holding 32-bits data, is necesary since in the code 64-bits and 32-bits registers are mixed.

Then, the local variables which are defined inside the function gets his value through an immediate:

```assem
000000014000100E mov    DWORD PTR [rbp-0Ch], 5      ; temp = 5
```

Then, the operations with the function values are performed, since data-copy between memory address is not allowed, the values with which the operations are going to be made must be passed to a register:

```assem
0000000140001015 mov    eax, DWORD PTR [rbp-4]      ; load a
```

Then, with the value in a register, the operation is performed and is stored in *result* local variable:

```assem
0000000140001018 add    eax, DWORD PTR [rbp-8]      ; add b
000000014000101B add    eax, DWORD PTR [rbp-0Ch]    ; add temp
000000014000101E mov    DWORD PTR [rbp-10h], eax    ; result = ...
```

Then, some redundance is performed and the epilogue of the stackframe is performed.

```assem
0000000140001021 mov    eax, DWORD PTR [rbp-10h]    ; return result
0000000140001024 add    rsp, 10h
0000000140001028 pop    rbp
0000000140001029 ret
```

Note than the stackframe epilogue only consist in lift the RSP the same amount of memory that were lowered in the prologue, there is no need to zeroed or clean the data since is enough to label the memory as unused to be reutilized again. The memory isn't actually "erased", it just becomes invalid/unreliable. The values might still be there until overwritten by the next function call.

The RET instruction is not part of the stackframe epilogue, is the counterpart of CALL and it pops out the next value on the stack on RIP register.

<br>

#### 3.3. Conclusion.

A few points taht are worth to have in mind are:

- Stackframe mechanism allocates space for the local variables. Modern x86-64 calling conventions require the stack to be 16-byte aligned before a CALL instruction. This means RSP must be divisible by 16. The compiler often allocates more space than strictly needed to maintain this alignment.

- Local variables are accessed using negative offsets from RBP: \[rbp-4\], \[rbp-8\], etc. The allocation and deallocation of the stackframe guarantee that local variable lifetime gets extended till the function termination. Without it, the local variable lifetime would also terminates with the local function termination but in a more caotic way and with more imprecissions. 


<br>

### 4. Array as a local variable. Imul, Movsx/zx.

Lets consider the following C code:

```c
short main() {
    short a;
    int b[6];
    long long c;
    a = 0xbabe;
    c = 0xbalb0abledbl100d;
    b[1] = a;
    b[4] = b [1] + c;
    return b[4];
}
```

The dissassembly is as follows:

```assem
0000000140001000  sub         rsp,38h  
0000000140001004  mov         eax,0FFFFBABEh  
0000000140001009  mov         word ptr [rsp],ax  
000000014000100D  mov         rax,0BA1B0AB1EDB100Dh  
0000000140001017  mov         qword ptr [c],rax  
000000014000101C  mov         eax,4  
0000000140001021  imul        rax,rax,1  
0000000140001025  movsx       ecx,word ptr [rsp]  
0000000140001029  mov         dword ptr b[rax],ecx  
000000014000102D  mov         eax,4  
0000000140001032  imul        rax,rax,1  
0000000140001036  movsxd      rax,dword ptr b[rax]  
000000014000103B  add         rax,qword ptr [c]  
0000000140001040  mov         ecx,4  
0000000140001045  imul        rcx,rcx,4  
0000000140001049  mov         dword ptr b[rcx],eax  
000000014000104D  mov         eax,4  
0000000140001052  imul        rax,rax,4  
0000000140001056  movzx       eax,word ptr b[rax]  
000000014000105B  add         rsp,38h  
000000014000105F  ret  
```

We can see that there are three new instructions, *imul*, *movsx*, *movzx*.

<br>

#### 4.1. IMUL - Signed Multiply.

This is an instruction that have three forms in base of the number of operands used with (one, two or three) and is the signed version of MUL (Unsigned Multiply). Let's start by the simplest form:

- *Two-operands* form: This is the more intuitive or predictable of the three forms. It just and extrapolation of the ADD/SUB instructions to the multiplication. It multiplies the destination by the source and store the result in the operand:

    ```assem
    imul dest, source --> dest = dest * source
    ```

    An example of usage can be:

    ```assem
    imul reg, r/mX
    ```

    Note that the operands cannot be two memory address at the same time.

<br>

- *Three-operands* form; This is an extension of the two-operands form but with an inmmediate acting as a scale of the source. The result is stored in the destination operand which is left out the operation:

    ```assem
    imul dest, source, immediate --> dest = source * immediate
    ```

    ```assem
    imul eax, ebx, 5 --> eax = ebx * 5
    ```

<br>

- *One-operand* form; In this case, IMUL gets reduced to an unary operation which gets the *two-operands* form using AX/EAX/RAX register as destination everytime.

    This is more complicated than what appears at first time, because multiply data often results in a size much larger than the size of the operands involved in the multiplication. Let's see an example:

    ```assem
    imul r/m8
    ```

    This operation is multiplying an 8-bit size by an 8-bit size generating a value that occupies 16-bit as maximum, lets do the maths:
    
    ```
    Maximum 8-bit value = 0b11111111 = 255
    Maximum 8^2-bit value =  255^2 = 65,025 < 65,535 = 0b1111111111111111 = Maximum 16-bit value
    ```
    
    **The general rule: multiplying an N-bit number by an N-bit number produces at most a 2N-bit result.**

    This essentially means that if we try to save the value in an 8-bit register like AL, the assembly operation would result in a truncated value. 
    
    So the solution, if the result of the operation cares, is in the majority of the cases to concatenate registers and store half of the bytes in one register and the other half in the other one. In the case of an 8-bit operation, remember that, in this case: AX = AH:AL --> AX is the concatenation of AH (the most significant byte) and AL (the less significant byte) 

    ```
    | <-- AX (16 bits) -> |
        AH (8) | AL (8)
    ```

    So, the operation would result in:

    ```
    imul r/m8 --> AX = AH:AL = AL * r/m8
    ```

    The same would apply to other widths:

    ```
    | Form | Operation | Result location |
    |------|-----------|-----------------|
    | IMUL r/m8 | AL × operand | AX = AH:AL (16-bit) |
    | IMUL r/m16 | AX × operand | DX:AX (32-bit) |
    | IMUL r/m32 | EAX × operand | EDX:EAX (64-bit) |
    | IMUL r/m64 | RAX × operand | RDX:RAX (128-bit) |
    ```

**This truncation mechanism only applies to the unary form of IMUL, in the binary o triary form truncation can happens.**

<br>

#### 4.2. MOVZX, MOVSX - Move with zero/sign extend.

This instructions move data from smaller register to a larger one and are very important when C performs a type conversion:

<br>

**MOVZX (Move with Zeri Extend)**

- Copies a smaller value to a larger destination
- Fills the upper bits with zeros
- Used for unsigned values
- Preserves the numeric value for unsigned integers

<br>

```
MOVZX dest, source
```

An example of usage could be:

```
MOV AL, 0xFF        ; AL = 11111111b (255)
MOVZX EAX, AL       ; EAX = 00000000 00000000 00000000 11111111b (255)
```

<br>

**MOVSX (Move with Sign Extend)**

- Copies a smaller value to a larger destination
- Fills the upper bits by repeating the sign bit (MSB)
- Used for signed values (2's complement)
- Preserves the numeric value for signed integers

```
MOVSX dest, source
```

As an example:

```
MOV AL, 0xFF        ; AL = 11111111b (-1 in signed)
MOVSX EAX, AL       ; EAX = 11111111 11111111 11111111 11111111b (-1)

MOV BL, 0x7F        ; BL = 01111111b (+127 in signed)
MOVSX EBX, BL       ; EBX = 00000000 00000000 00000000 01111111b (+127)
```

<br>

**Explanation of the use of each instruction**

Then, for example, if we have a C code and we assign a *short* to a wider value like an *unsigned integer*, then we don't just use MOV, since that would preserve the size, we use MOVZX to convert the value to a positive size-extended version of it self (2 bytes --> 4 bytes):

```c
; short s = -5
mov     word ptr [rsp+10h], 0FFFBh    ; -5 in twos complement (16-bit)

; unsigned int u = s
movsx   eax, word ptr [rsp+10h]       ; sign-extend to 32-bit: 0xFFFFFFFB
mov     dword ptr [rsp+14h], eax      ; store as unsigned (interprets as 4294967291)

; int i = s
movsx   eax, word ptr [rsp+10h]       ; sign-extend to 32-bit: 0xFFFFFFFB
mov     dword ptr [rsp+18h], eax      ; store as signed (interprets as -5)
```

If instead we assign to a *signed integer*, then we use MOVSX in order to extend the size of the value preserving the sign (or giving a sign if wasn't there before).

```c
; unsigned short us = 65531
mov     word ptr [rsp+10h], 0FFFBh

; unsigned int u = us
movzx   eax, word ptr [rsp+10h]       ; zero-extend: 0x0000FFFB (65531)
mov     dword ptr [rsp+14h], eax

; int i = us
movzx   eax, word ptr [rsp+10h]       ; zero-extend: 0x0000FFFB (65531)
mov     dword ptr [rsp+18h], eax
```

<br>

#### 4.3. Understanding arrays in assembly.

Now that we understood IMUL, MOVSX and MOVZX instructions, we can introduce how assembly handles array structures.

Local variables gets accesed via directs stack offsets using RBP register as we see in previous examples. This is possible since the compiler knows the exact location of a local variable since this are defined (this is, they get a value) within the function.

How ever, a value within an array takes other perspective, lets consider the following C code:

```c
void set_element(int arr[], int i, int value) {
    arr[i] = value; 
}
```

On it, *i* is an unknown variable from the compiler perspective and thus it can't assign value parameter to a specific memory address as if were a local variable instead, it have to make that assignation dependant on the value of *i* which gets defined at runtime.

The formula is:

```
base_array_address + (index × element_size)
```

Note that, an array is nothing but a linear chunk of memory, we need to multiply the index by the scale of the datatype in order to map the address in which the slot denoted by the index is in the stack. The later addition with 'base_array_address' is just an ordinary way to find an address thorough 'pointer + offset'

And it applies at every array, note that in the example provide in the code above (presented again just below), the array assignation is everytime through constants (known by the compiler) so in fact the compiler knows the offset to access that specific memory address and it could accessed through stack offsets but it doesn't because the standadrd method is what is explained above.

So, let's see how this formula is implemented in assembly when an array is presented.

Consider the following code:

```c
int main(){
    char buff[10];
    char a = 'A';
    buff[5] = a;
    return 0;
}
```

This code declares an array of chars of 10 slots, and a local variable then it performes an assignation and then returns. Note that arrays gets allocated in the stack despite the uses of them; stackframe expands enough to hold every declaration inside the function.


Consider the following disassembly:

```assem
0000000140001000 48 83 EC 28          sub         rsp,28h  
0000000140001004 C6 04 24 41          mov         byte ptr [rsp],41h  
0000000140001008 B8 01 00 00 00       mov         eax,1  
000000014000100D 48 6B C0 05          imul        rax,rax,5  
0000000140001011 0F B6 0C 24          movzx       ecx,byte ptr [rsp]  
0000000140001015 88 4C 04 08          mov         byte ptr buff[rax],cl  
0000000140001019 33 C0                xor         eax,eax  
000000014000101B 48 83 C4 28          add         rsp,28h  
000000014000101F C3                   ret 
```

In order to be able to apply the formula mentioned above, we need first to calculate index address, which is performed in the following instruction:

```assem
0000000140001008 B8 01 00 00 00       mov         eax,1 //Copy the size of the datatype (this time, char = 1) on the rax register.
000000014000100D 48 6B C0 05          imul        rax,rax,5 //Then perform the multiplication using imul with rax register and the index; 5.
```

Now RAX register contains the offset (5) to be used along with the base address of the buffer. There is no ADD instruction since the processor already perform automatically that addition when perform the memory access, it just calculates de offset, stored it in RAX and then uses RAX in the following instruction:

```assem
0000000140001011 0F B6 0C 24          movzx       ecx,byte ptr [rsp]  
0000000140001015 88 4C 04 08          mov         byte ptr buff[rax],cl
```

Which is accesssing that offset from the base_address of the buffer (buff), when accesing that memory address, copy the byte *cl* and then goes on.

The *buff* is addressing mode, is resolved by the disassembler to mean "rsp + 0x8 + rax" (rsp + 0x8 is where the buffer starts on the stack). The full address computation would be: 

```assem
rsp + 0x8 + rax == [rsp + 0x8] + (5 * 1)
```

satisfying the equation mentioned above.


Also, is convenient to say that the code above is MCVS being extraordinary unefficient. Moder compilers like gcc would resolve the memory access to the *buff* as if were a local variable since the index is hardcoded and the compiler knows at compile-time what that index is so there's no need to implement IMUL operations and make the assignation dependant on an unknown variable.

If we compile the code above with gcc and open it with radare2 we would get:

```
$ r2 -e asm.sub.var=false -A -qc "s main; pdf" test
Warning: run r2 with -e bin.cache=true to fix relocations in disassembly
            ; DATA XREF from entry0 @ 0x1078
┌ 65: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_13h @ rbp-0x13
│           ; var int64_t var_dh @ rbp-0xd
│           ; var int64_t var_8h @ rbp-0x8
│           0x00001149      f30f1efa       endbr64                               ; Intel CET Instruction
│           0x0000114d      55             push rbp                              ; Stackframe prologue
│           0x0000114e      4889e5         mov rbp, rsp
│           0x00001151      4883ec20       sub rsp, 0x20
│           0x00001155      64488b042528.  mov rax, qword fs:[0x28]              ; Stack canary (BOF security measure)
│           0x0000115e      488945f8       mov qword [rbp - 8], rax              
│           0x00001162      31c0           xor eax, eax
│           0x00001164      c645ed41       mov byte [rbp - 0x13], 0x41 ; 'A'     ; char a = 'A'
│           0x00001168      0fb645ed       movzx eax, byte [rbp - 0x13]          ; buff[5] = a;
│           0x0000116c      8845f3         mov byte [rbp - 0xd], al
│           0x0000116f      b800000000     mov eax, 0                            ; return 0
│           0x00001174      488b55f8       mov rdx, qword [rbp - 8]              ; Check stack canary
│           0x00001178      64482b142528.  sub rdx, qword fs:[0x28]
│       ┌─< 0x00001181      7405           je 0x1188
│       │   0x00001183      e8c8feffff     call sym.imp.__stack_chk_fail
│       │   ; CODE XREF from main @ 0x1181
│       └─> 0x00001188      c9             leave
└           0x00001189      c3             ret      
```

As we can see, since the index is hardcode, the compiler already knows where is the referenced slot of the array exists in the stack:

```
0x00001168      0fb645ed       movzx eax, byte [rbp - 0x13]
0x0000116c      8845f3         mov byte [rbp - 0xd], al
```

So, in conclusion, both forms of handle arrays exists and are completely valid.

<br>

### 5. Struct Local Variable.

Like *arrays*, *structs* in C are linear memory regions which are accesibles due to offset arithmetics but containing different datatypes elements. 

An important concept on how the compiler deals with the allocation of memory for a structure is the *memory alignment principle* which leaks in *structure padding*.

<br>

#### 5.1. Mermoy Alignment Principle.

Memory alignment refers to how data is positioned in memory relative to addresses that are multiples of certain values (typically powers of 2).

The fundamental reason is architectural and we already ass through it; CPUs access and work data through some special integrated devices called *registers* which have the width of a *word* (8 bytes in x64 architectures), it don't fetch memory byte-by-byte. This mean that in a CPU cycle, the CPU reach exactly 8 bytes of data. So, consider the following example.

Let's suppouse we have 16 byes of data, this corresponds to two CPU cycles, this means, it takes (ideally) two times to the CPU to read the data stored in those bytes, then let's suppose we have a long integer (8 bytes) occuping the half of thos 16 bytes, 4 in one octet and 4 in other octet. In order to be able to read the long the CPU would need two times instead of the minimum required per the size of the data type:

<br>

MEMORY LAYOUT: MISALIGNED LONG (8 bytes spanning two octets)

                    ┌───────────────────────────────────────────────────────────────┐
                    │                      16 BYTES OF MEMORY                       │
                    ├───────────────────────────────┬───────────────────────────────┤
                    │         FIRST OCTET           │        SECOND OCTET           │
                    │    (CPU Cycle 1 - 8 bytes)    │   (CPU Cycle 2 - 8 bytes)     │
                    ├───┬───┬───┬───┬───┬───┬───┬───┼───┬───┬───┬───┬───┬───┬───┬───┤
                    │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │13 │14 │15 │
                    ├───┴───┴───┴───┼───┴───┴───┴───┴───┴───┴───┴───┼───┴───┴───┴───┤
                    │   (unused)    │◄──────── LONG (8 bytes) ─────►│   (unused)    │
                    │   4 bytes     │     4 bytes   │    4 bytes    │    4 bytes    │
                    └───────────────┴───────────────┴───────────────┴───────────────┘
                                                    ▲
                                                    │
                                        OCTET BOUNDARY (address 0x08)


                    PROBLEM: To read the misaligned LONG, the CPU must:

                        ┌─────────────────┐         ┌─────────────────┐
                        │   CPU Cycle 1   │         │   CPU Cycle 2   │
                        │  Fetch bytes    │         │  Fetch bytes    │
                        │    0x00-0x07    │         │    0x08-0x0F    │
                        │                 │         │                 │
                        │  Extract bytes  │         │  Extract bytes  │
                        │    4, 5, 6, 7   │         │   8, 9, 10, 11  │
                        └────────┬────────┘         └────────┬────────┘
                                │                           │
                                └───────────┬───────────────┘
                                            ▼
                                ┌───────────────────────┐
                                │  Combine fragments    │
                                │  into complete LONG   │
                                └───────────────────────┘

                RESULT: 2 CPU cycles for data that should require only 1


<br>

This is extremely inefficient, the solution: force the data storage to start in a multiple of a word's address. 

Thus, if we know for example have two integers (4 bytes each) and a char intercalates between each integer, then the data in memory would be stored following the memory allignment principle:


                ┌───────────────────────────────────────────────────────────────┐
                │                      16 BYTES OF MEMORY                       │
                ├───────────────────────────────┬───────────────────────────────┤
                │         FIRST WORD            │         SECOND WORD           │
                │         (8 bytes)             │          (8 bytes)            │
                ├───┬───┬───┬───┬───┬───┬───┬───┼───┬───┬───┬───┬───┬───┬───┬───┤
                │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │12 │13 │14 │15 │
                ├───┴───┴───┴───┼───┼───┴───┴───┼───┴───┴───┴───┼───┴───┴───┴───┤
                │◄─ int a ─────►│ c │◄── gap ──►│◄─── int b ───►│  (available)  │
                │    4 bytes    │(1)│  3 bytes  │    4 bytes    │    4 bytes    │
                └───────────────┴───┴───────────┴───────────────┴───────────────┘
                                                ▲
                                                │
                                WORD BOUNDARY (address 0x08)

Observe two things:

- First, te char datatype is inside the first chunk because, per its size, the value fits in the gap leaved by the integer before inside the first word. This means that allignment don't force every data value to be stored in a brand new 8-multiple-address-start octet, just those data values that don't fit in the gap leave by other data stored before. This is the case of integer b (4 bytes can't be stored on a 3-bytes gap) so it corresponds to be stored in a new correspondly alligned octet.

- There exists unused bytes in memory (in our case, 5, 6 and 7) which corresponds to those bytes that fills gaps between alligned datatypes. Since memory has a linear nature, this bytes are lost and will never be reused until memory gets released more likely when program terminates most of the time.

Since the two reasons above, the rule gets slitly changed to a more efficient approach: *a data type should be stored at an address that's a multiple of its own size*. A 4-byte int at multiples of 4, an 8-byte long at multiples of 8, a 2-byte short at multiples of 2, and a 1-byte char anywhere (since every address is a multiple of 1). This is what we call *memory principle allignment*, and guarantee no data value gets stored between two CPU cycles.

<br>

#### 5.2. Structure Padding.

The *memory alignment principle* applies every time data is stored in memory however some C entities does not seems to be affected, local variables or arrays are some examples. Arrays are linear memory regions reserved for same datatype values, then a fixed-size array of a specific datatype will always occupies the same, and barely equal for local variables.

However, there is a problem when we talk about structures. We know that the size of a structure is the addition of the size of the fields that composes the struct.

So if we get the following C code:

```c
#include <stdio.h>

typedef struct my_struct {
    int a;
    char b;
    int c;
} struct_1;

int main(){
    struct_1 foo;
    printf("This struct is %ld bytes width", sizeof(foo));
    return 0;
}
```

We should spect that the output would be something like:

```less
OUTPUT:

    This struct is 9 bytes width

```

But if we compile the code and check the result we will find out that is not, the actual size is 12. This is because we are no taking in consideration the unsued 3 left bytes between the char and the second integer due to memory alignment. The real count is:

```less
int a + char b + unused bytes + int c = 4 + 1 + 3 + 4 = 12
```

                    12 BYTES OF STRUCTURE MEMORY

        ├───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐               
        │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │11 │               
        ├───┴───┴───┴───┼───┼───┴───┴───┼───┴───┴───┴───┤               
        │◄─── int a ───►│ b │◄─padding─►│◄─── int c ───►│               
        │    4 bytes    │(1)│  3 bytes  │    4 bytes    │               
        └───────────────┴───┴───────────┴───────────────┘               
                            ▲           ▲                               
                            │           │                               
                      offset 4      offset 8                            
                    (4 % 1 = 0 ✓)  (8 % 4 = 0 ✓)                       
        ──────────────────────────────────────────────────


This effect is known as *structure padding*, when a C compiler automatically inserts extra bytes into a struct to align its members in memory.

Structure padding is a consecuence of the memory allignement and actually exists beyond structures, it affects on how memory gets alloced along a linear region in a huge amount of posibles combinations (nested structures, structures with arrays, arrays of structures, etc).

<br>

#### 5.3. Structures Dissasembly.

Consider the following C code:

```c
typedef struct mystruct {
    short a;
    int b[6];
    long long c;
} mystruct_t;

short main() {
    mystruct_t foo;
    foo.a = 0xbabe;
    foo.c = 0xba1b0ab1edb100d;
    foo.b[1] = foo.a;
    foo.b[4] = foo.b[1] + foo.c;
    return foo.b[4];
}
```

This C code defines an structure with several datatypes including an array. This the memory layout of this structure is:

-> 2 bytes for short a
-> 2 bytes for padding
-> 4*6 contiguous bytes for each array entry
-> 4 bytes for padding (since 24 mod 8 = 0 but array started in non-aligned address)
-> 8 bytes (word) for long long c

In total, 40 bytes, note that the stackframe expands 0x38, which is enough for the structure.

If we compile the code in MCVS 2019, we obtain the following dissasembly:

```less
0000000140001000 48 83 EC 38          sub         rsp,38h  
0000000140001004 B8 BE BA FF FF       mov         eax,0FFFFBABEh  
0000000140001009 66 89 04 24          mov         word ptr [rsp],ax  
000000014000100D 48 B8 0D 10 DB 1E AB B0 A1 0B mov         rax,0BA1B0AB1EDB100Dh  
0000000140001017 48 89 44 24 20       mov         qword ptr [rsp+20h],rax  
000000014000101C B8 04 00 00 00       mov         eax,4  
0000000140001021 48 6B C0 01          imul        rax,rax,1  
0000000140001025 0F BF 0C 24          movsx       ecx,word ptr [rsp]  
0000000140001029 89 4C 04 04          mov         dword ptr [rsp+rax+4],ecx  
000000014000102D B8 04 00 00 00       mov         eax,4  
0000000140001032 48 6B C0 01          imul        rax,rax,1  
0000000140001036 48 63 44 04 04       movsxd      rax,dword ptr [rsp+rax+4]  
000000014000103B 48 03 44 24 20       add         rax,qword ptr [rsp+20h]  
0000000140001040 B9 04 00 00 00       mov         ecx,4  
0000000140001045 48 6B C9 04          imul        rcx,rcx,4  
0000000140001049 89 44 0C 04          mov         dword ptr [rsp+rcx+4],eax  
000000014000104D B8 04 00 00 00       mov         eax,4  
0000000140001052 48 6B C0 04          imul        rax,rax,4  
0000000140001056 0F B7 44 04 04       movzx       eax,word ptr [rsp+rax+4]  
000000014000105B 48 83 C4 38          add         rsp,38h  
000000014000105F C3                   ret  
```

Now, lets read the assembly code:

- First, the stackframe prologue:

    ```
    sub         rsp,38h 
    ```

- Asignations and operations:

    ```c
    foo.a = 0xbabe;
    ```

    ```
    0000000140001004 B8 BE BA FF FF       mov         eax,0FFFFBABEh  
    0000000140001009 66 89 04 24          mov         word ptr [rsp],ax
    ```

    First, the value "0FFFFBABEh" gets writted to eax, then 'ax' (the lower 16 bits of rax) are written to the left word of the contents of rsp. Remember that rsp points to the top of the stack, this means that the alocation in the stack has been done in opposite direction of the definition in the structure. 

    <br>

    ```c
    foo.c = 0xba1b0ab1edb100d;
    ```

    ```
    000000014000100D 48 B8 0D 10 DB 1E AB B0 A1 0B   mov         rax,0BA1B0AB1EDB100Dh  
    0000000140001017 48 89 44 24 20                  mov         qword ptr [rsp+20h],rax  
    ```

    Then, the value "0BA1B0AB1EDB100Dh" gets stored and rax and then, on 'rsp + 0x20'. Let's do some counts here: 0x20 = 2*16^1 + 0\*16^0 = 32 bytes, this would not be possible if there was no padding, since the teorically distant between those two fields is 28 bytes (24 + 4).

    <br>

    ```c
    foo.b[1] = foo.a;
    ```

    ```
    000000014000101C B8 04 00 00 00       mov         eax,4  
    0000000140001021 48 6B C0 01          imul        rax,rax,1  
    0000000140001025 0F BF 0C 24          movsx       ecx,word ptr [rsp]  
    0000000140001029 89 4C 04 04          mov         dword ptr [rsp+rax+4],ecx  
    ```

    As we see in the array part, MCSV uses the IMUL method to calculate the offset throught the index and the datatype size and then solves 'base_address + index*element_size' (rsp+rax+4). Then it gets the value from rsp (a) and copy it on the rsp+rax+4 address.

    Note also that with this assignation, we are converting a *short* (a) to a *signed integer*, thus, when "rsp" is copied to "ecx" to later be copied to "rsp + rax + 4", MOVSX is being used in order to give the value a sign (if it was an unsigned int, MOVZX would be used instead).

    <br>

    ```c
    foo.b[4] = foo.b[1] + foo.c;
    ```

    ```
    000000014000102D B8 04 00 00 00       mov         eax,4  
    0000000140001032 48 6B C0 01          imul        rax,rax,1  
    0000000140001036 48 63 44 04 04       movsxd      rax,dword ptr [rsp+rax+4]  
    000000014000103B 48 03 44 24 20       add         rax,qword ptr [rsp+20h]  
    0000000140001040 B9 04 00 00 00       mov         ecx,4  
    0000000140001045 48 6B C9 04          imul        rcx,rcx,4  
    0000000140001049 89 44 0C 04          mov         dword ptr [rsp+rcx+4],eax 
    ```


    First, fetch "foo.b\[1\]" and stores its value in rax, then gets "foo.c" and adds that value to rax, now rax contains "foo.b\[1\] + foo.c" and this value gets stored on fourth slot of the array.

    <br>

    ```c
    return foo.b[4];
    ```

    ```
    0000000140001056 0F B7 44 04 04       movzx       eax,word ptr [rsp+rax+4]  
    000000014000105B 48 83 C4 38          add         rsp,38h    ; Stackframe epilogue
    000000014000105F C3                   ret 
    ```

### 6. Instruction exercises.

#### 6.1. MOVZX exercises

What value is in r14 after this code executes?

```assem
mov r12, 0x5B542050674CD692
movzx r14, r12b
```

First, "0x5B542050674CD692" value gets copied over r12, then r12b gets copied over r14. r12b is accessing the lowest byte of r12 register which is 0x92, copying onto r14 and zeroing the rest of uppers bytes, so r14 has 0x0000000000000092 value.

<br>

What value is in r12w after this code executes?

```assem
mov di, 0x4B39
mov r13w, 0x6396
movzx r12w, r13b
```

Then, it moves 2-bytes hexadecimal value to r13w which is the 16 lowest bits of r13 register, then moves the lowest byte of r13, which is 0x96, to the 16 lowest bits of r12 and zeroup the rest of bytes of the 16 bits within r12w. So de answer would be 0x0096

<br>

What value is in rdx after this code executes?

```assem
mov rdi, 0xBCE7AA1E4633FA15
add rdi, 0x4375165316635F7B
movzx rdx, dil
```

dil the lower byte of rdi has 0x90.

<br>

#### 6.2. MOVSX exercises.

What value is in esi after this code executes?

```
mov rsp, 0xA440031B065793D1
movsx esi, sp
```

The first instruction moves 0xA440031B065793D1 over rsp. Then, moves with sign extension sp, which is the 16 lowest bits of rsp, to esi.

MOVSX is an isntruction that oneup or zeroup depending of the sign of the value. So first, we have to tell if the value is positive or negative:

```assem
rsp (64 bits) --> 0xA440031B065793D1; sp (16 bits) --> 0x93D1 --> 0b1001001111010001
```

Per the first byte convention, the value is negative and this means that this value would be extended like follows:

```assem
sp --> 0b1001001111010001 MOVSX esi --> 0b1111111111111111001001111010001 -> 0xFFFF93D1
```

<br>

What value is in r10 after this code executes?

```
mov r10d, 0x67C1ABD2
mov r8d, 0x7CBE1AFF
movsxd r10, r8d
```

As we did before, r8d contents (doubleword is double of a word, 32-bits) is being moved with sign extension to r10, so first lets check the sign converting it to binary:

```
0x7CBE1AFF --> 0b01111100101111100001101011111111
```

thus, the value is positive an the value in r10 must be zero-extended:

```
r10 --> 0x000000007CBE1AFF
```