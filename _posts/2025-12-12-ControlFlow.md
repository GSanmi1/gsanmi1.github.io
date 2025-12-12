---
layout: post
title: Control Flow.
subtitle: Unconditional and conditional x86-64 instructions.
tags: [assem]
---

### 1. Control Flow. Definition and types.

In terms of program execution; **Control Flow** is a term that refers in the order in which the instructions gets executed by the CPU. Generally, in simple terms, there is a special non-general-purpouse register (RIP on x64) that holds the address of the next instruction to be executed and advanced sequentially through memory if nothing interrupts it.

How ever, many architectures implements a set of instructions that allows a program to take over the control flow manipulating RIP under certain circunstances in two ways:

- **Unconditional**; execution always transfers somewhere else regardless of state, examples of this control flow take-away are instructions like CALL or RET.
- **Conditional**, which divides the code into branchs based on test cases triggered by some instructions.


<br>

### 2. Unconditional Control Flow.

#### 2.1. Goto, JMP Instruction.

Consider the following C code:

```c
int main(){
	goto mylabel;
	printf("skipped\n");
mylabel:
	printf("goto ftw!\n");
	return 0xb01dface;
}
```

This code make use of the *goto* directive which reference some label in the code (mylabel), which skips all the code between that line and the label and starts executing from that point.

The MCVS 2019 disassembly shows the following:

```assem
0000000140001000 48 83 EC 28          sub         rsp,28h  ;shadow space as MCVS 2019 it follows Microsoft ABI x64 standard
0000000140001004 EB 0C                jmp         $mylabel (0140001012h)  ; JMP go directly to address of the value between brackets (0000000140001012)
0000000140001006 48 8D 0D F3 4F 00 00 lea         rcx,[__NULL_IMPORT_DESCRIPTOR+1580h (0140006000h)]  
000000014000100D E8 7E 00 00 00       call        printf (0140001090h)  
0000000140001012 48 8D 0D F7 4F 00 00 lea         rcx,[__NULL_IMPORT_DESCRIPTOR+1590h (0140006010h)]  ; Includes the parameter value into RCX register to pass it to printf()
0000000140001019 E8 72 00 00 00       call        printf (0140001090h) ; CALL printf()  
000000014000101E B8 CE FA 1D B0       mov         eax,0B01DFACEh  ; moves the return value into EAX
0000000140001023 48 83 C4 28          add         rsp,28h  ;
0000000140001027 C3                   ret  
```

Note that in this dissasembly, since MCVS 2019 is extremely inneficient, there is code that is never executed which is the code involving the first printf() call which is skipped.

And the GCC dissasembly:

```assem
            ; DATA XREF from entry0 @ 0x1078
┌ 31: int main (int argc, char **argv, char **envp);
│           0x00001149      f30f1efa       endbr64
│           0x0000114d      55             push rbp ; Stackframe prologue.
│           0x0000114e      4889e5         mov rbp, rsp
│           0x00001151      90             nop
│           0x00001152      488d05ab0e00.  lea rax, str.goto_ftw_      ; 0x2004 ; "goto ftw!" ; Include the string into the RDI to pass this value as a parameter to puts()
│           0x00001159      4889c7         mov rdi, rax                ; const char *s
│           0x0000115c      e8effeffff     call sym.imp.puts           ; int puts(const char *s) ; CALL puts()
│           0x00001161      b8cefa1db0     mov eax, 0xb01dface         ; return value
│           0x00001166      5d             pop rbp                     ; Stackframe epilogue
└           0x00001167      c3             ret
```

Lets observe several things between the two dissasemblies:

- First, unexecuted code has been removed, in the MCSV 2019 code, there was two printf() calls and a JMP statement which deflects the control flow over an address making part of the code unused. In this case, this part is removed and the goto directive is converted to a NOP instruction (No-operation).

- The second is that instead of call to printf(), is calling puts() since printf() has being called with no format options and puts is simplier.

<br>

Lets talk a bit about JMP. The JMP instruction is one of the most fundamental control flow instructions in assembly language. It performs an unconditional jump to a specified location in code, transferring program execution to a different address.

```
JMP destination
```

Where destination can be:

- A label (most common).
- A register containing an address.
- A memory location containing an address
- An immediate address (direct address)

JMP modifies the instruction pointer (IP/EIP/RIP) to point to the destination address, in this terms JMP would be equal as:

```assem
MOV RIP, destination
```

We can encounter some variants of JMP related on the encoding size and addresing range. For small jumps is more efficient to use shorter versions of JMP:

- **JMP SHORT**, encoded in two bytes, the operand is a signed 8-bit offset from the next instruction. Range: -128 to +127 bytes. Very compact, commonly used for small local jumps like skipping a few instructions.

- **JMP NEAR**; encoded in 5 bytes, the operand is a signed 32-bit offset within the same code segment.

- **JMP FAR**; encoded in more than 7 bytes, the operand is in a different code segment.

<br>

A quick reminder of all the covered unconditional control flow instructions:

| Instruction | Type                       | Stack Impact          | Use Case                |
|-------------|----------------------------|-----------------------|-------------------------|
| JMP         | Unconditional Control Flow | None                  | Direct control transfer |
| CALL        | Unconditional Control Flow | Pushes return address | Function calls          |
| RET         | Unconditional Control Flow | Pops return address   | Function returns        |

<br>

### 3. Conditional Control Flow.

Conditional control flow allows programs to make decisions and execute different code paths based on runtime conditions.

<br>

#### 3.1. FLAGS register (RFLAGS in x64 bits).

The FLAGS register, originally 16-bits, EFLAGS in 32-bit and RFLAGS in 64-bit, is a special-purpose register that holds status information about the result of the most recent arithmetic or logical operation, plus control bits that affect CPU behavior.

**EFLAGS Register Layout (32-bit)**
```
Bit:  31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    | 0| 0| 0| 0| 0| 0| 0| 0| 0| 0|ID|VP|VF|AC|VM|RF|  |NT| IOPL |OF|DF|IF|TF|SF|ZF|  |AF|  |PF|  |CF|
    |  |  |  |  |  |  |  |  |  |  |  |IP|IF|  |  |  | 0|  |      |  |  |  |  |  |  | 0|  | 0|  | 1|  |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
```

The 32 uppers bits of RFLAGS are set to 0 and not used.

<br>

**Flag Definitions**

| Bit | Flag | Full Name | Type |
|-----|------|-----------|------|
| 0 | CF | Carry Flag | Status |
| 2 | PF | Parity Flag | Status |
| 4 | AF | Auxiliary Carry Flag | Status |
| 6 | ZF | Zero Flag | Status |
| 7 | SF | Sign Flag | Status |
| 8 | TF | Trap Flag | System |
| 9 | IF | Interrupt Enable Flag | System |
| 10 | DF | Direction Flag | Control |
| 11 | OF | Overflow Flag | Status |
| 12-13 | IOPL | I/O Privilege Level | System |
| 14 | NT | Nested Task | System |
| 16 | RF | Resume Flag | System |
| 17 | VM | Virtual-8086 Mode | System |
| 18 | AC | Alignment Check | System |
| 19 | VIF | Virtual Interrupt Flag | System |
| 20 | VIP | Virtual Interrupt Pending | System |
| 21 | ID | ID Flag | System |

<br>

**Flag Types**

| Type | Description |
|------|-------------|
| S (Status) | Modified by arithmetic/logical instructions (CF, PF, AF, ZF, SF, OF) |
| C (Control) | Controls CPU behavior for string operations (DF) |
| X (System) | Used by OS/hardware, privileged operations |

<br>

**Reserved Bits**

| Bit | Fixed Value |
|-----|-------------|
| 1 | Always 1 |
| 3 | Always 0 |
| 5 | Always 0 |
| 15 | Always 0 |
| 22-31 | Always 0 |

**Note:** Reserved bit positions should not be modified. Always preserve their values when writing to EFLAGS.

Each bit in FLAGS represents a specific condition which manifest as a specific flag with his own iterpretation:

- **ZF (Zero Flag)**: set to 1 if the result was zero.

- **SF (Sign Flag)**: reflects the most significant bit of the result, indicating whether it's negative in signed interpretation.

- **CF (Carry Flag)**: set when an unsigned operation overflows or underflows, (if you add two 32-bit values and the result needs a 33rd bit, CF gets set).

- **OF (Overflow Flag)**: set when a *signed operation* produces a result that doesn't fit in the destination. This happens when adding two positive numbers gives a negative result (or vice versa).

- **PF (Parity Flag)**: set if the low byte of the result has an even number of 1-bits. Mostly a legacy thing, occasionally used in floating-point comparisons.

- **AF (Auxiliary Carry Flag)**: carry out of bit 3, used for BCD arithmetic. You'll rarely see this in modern code.

<br>

| Flag            | Bit | Set when...                     |
|-----------------|-----|---------------------------------|
| **ZF** (Zero)   | 6   | Result is zero                  |
| **SF** (Sign)   | 7   | Result is negative (MSB = 1)    |
| **CF** (Carry)  | 0   | Unsigned overflow/underflow     |
| **OF** (Overflow) | 11  | Signed overflow                 |

<br>

FLAGS is fundamentally different from general-purpose registers. It's not a register you manipulate directly with x64 instructions (like MOV), instead, it's automatically updated as a side effect of arithmetic and logical operations (barely allmost of the instructions that performs an arithmetic/logical operation do internally modify bits from the FLAGS register), and then read implicitly by teh so called "conditional instructions".

User almost never read directly FLAGS register, instead, use instructions which implicitly check specific bits of the register and act on them, this is what are known as the *Conditional Instructions*.

<br>

#### 3.2. Conditional Instructions.

##### 3.2.1. CMP, Compare.

CMP (compare) is used to compare two operands by performing a subtraction without storing the result. It only modifies the FLAGS register, with which subsequent conditional instruction will make decisions.

The sintax is:

```
CMP destination, source
```

Where destination and source can be memory address in form of r/mX, register, or immediate value (You cannot compare memory-to-memory directly; one operand must be a register or immediate). 


Internally, CMP computes *destination - source* and discards the result, but sets flags based on what that result would have been. This is identical to SUB except the destination remains unchanged.

Thus, for example, and in order to provide full ilustration about the FLAGS register behaviour, when the CPU executes CMP, it review the result and modify some bit on FLAGS register , for example:

- If destination == source, subtraction yields 0, and ZF (6th bit) is set to one.
- If destination != source, and the most significant byte of the result is 1, then the result is negative as a signed value and SF (7th bit) is set up.

Note that depending that if it is signed or unsigned comparison different bit-flags would be affeced.

And so on.

<br>

##### 3.2.2. TEST, logical comparison.

TEST instruction is the logical equivalent of what CMP is to SUB—a non-destructive way to check conditions.

TEST performs a bitwise AND between two operands, discards the result, and updates FLAGS based on what that result would have been.

```assem
TEST destination, source
```

Where *destination* and *source* can be either a register, a memory address in *r/mX* form and an immediate value (rememeber that operation between memory address are not allowed). 

Internally computes "destination AND source", throws away the result, sets flags. The operands remain unchanged (the difference between AND and TEST is that AND stores the result while TEST not). 

<br>

| Flag | Behavior |
|------|----------|
| ZF | Set if result is zero (no overlapping bits) |
| SF | Copies MSB of result (sign in two's complement interpretation) |
| PF | Set if low byte has even number of 1-bits |
| CF | Always cleared to 0 |
| OF | Always cleared to 0 |
| AF | Undefined |

<br>

##### 3.2.3. Arithmetic Instructions.

Most arithmetic operations (ADD, SUB, AND, OR, XOR, etc.) also set flags.

<br>

##### 3.2.4. Conditional Jump Instructions. Jcc.

As we saw before, JMP is an instruction that control unconditionally the flow of execution of the program by modifying RIP instruction with a destination address. 

In conditional control flow, there are conditional variants of JMP instruction. This is, instructions that behaviours as JMP under certains circunstances; if a condition is true, the jump is taken:

| jmp variant | Condition | Description |
|-------------|-----------|-------------|
| je/jz | ZF = 1 | Jump if equal/zero |
| jne/jnz | ZF = 0 | Jump if not equal/not zero |
| js | SF = 1 | Jump if negative |
| jns | SF = 0 | Jump if non-negative |
| jg/jnle | ZF=0 & SF=OF | Jump if greater (signed) |
| jge/jnl | SF = OF | Jump if greater or equal (signed) |
| jl/jnge | SF ≠ OF | Jump if less (signed) |
| jle/jng | ZF=1 or SF≠OF | Jump if less or equal (signed) |
| ja/jnbe | CF=0 & ZF=0 | Jump if above (unsigned) |
| jae/jnb | CF = 0 | Jump if above or equal (unsigned) |
| jb/jnae | CF = 1 | Jump if below (unsigned) |
| jbe/jna | CF=1 or ZF=1 | Jump if below or equal (unsigned) |
| jo | OF = 1 | Jump if overflow |
| jno | OF = 0 | Jump if not overflow |

Note that, besides there are different instructions names (like for example je and jz), al behaves the same way if a condition is met and in order to check that condition both consults the same bit-flag from the RFLAGS register. Thus, to conditional jumps are equals o the same if checks the same bit-flag (lie je and jz).

<br>

##### 3.2.5. Conditional Moves and Set.

As well as conditional jumps, there are also conditional moves:

| Instruction | Condition | Description |
|-------------|-----------|-------------|
| cmove/cmovz | ZF = 1 | Move if equal/zero |
| cmovne/cmovnz | ZF = 0 | Move if not equal/not zero |
| cmovs | SF = 1 | Move if negative |
| cmovns | SF = 0 | Move if non-negative |
| cmovg/cmovnle | ZF=0 & SF=OF | Move if greater (signed) |
| cmovge/cmovnl | SF = OF | Move if greater or equal (signed) |
| cmovl/cmovnge | SF ≠ OF | Move if less (signed) |
| cmovle/cmovng | ZF=1 or SF≠OF | Move if less or equal (signed) |
| cmova/cmovnbe | CF=0 & ZF=0 | Move if above (unsigned) |
| cmovae/cmovnb | CF = 0 | Move if above or equal (unsigned) |
| cmovb/cmovnae | CF = 1 | Move if below (unsigned) |
| cmovbe/cmovna | CF=1 or ZF=1 | Move if below or equal (unsigned) |
| cmovo | OF = 1 | Move if overflow |
| cmovno | OF = 0 | Move if not overflow |

And conditional set bits:

| Instruction | Condition | Description |
|-------------|-----------|-------------|
| sete/setz | ZF = 1 | Set byte if equal/zero |
| setne/setnz | ZF = 0 | Set byte if not equal/not zero |
| sets | SF = 1 | Set byte if negative |
| setns | SF = 0 | Set byte if non-negative |
| setg/setnle | ZF=0 & SF=OF | Set byte if greater (signed) |
| setge/setnl | SF = OF | Set byte if greater or equal (signed) |
| setl/setnge | SF ≠ OF | Set byte if less (signed) |
| setle/setng | ZF=1 or SF≠OF | Set byte if less or equal (signed) |
| seta/setnbe | CF=0 & ZF=0 | Set byte if above (unsigned) |
| setae/setnb | CF = 0 | Set byte if above or equal (unsigned) |
| setb/setnae | CF = 1 | Set byte if below (unsigned) |
| setbe/setna | CF=1 or ZF=1 | Set byte if below or equal (unsigned) |
| seto | OF = 1 | Set byte if overflow |
| setno | OF = 0 | Set byte if not overflow |

<br>

### 4. Examples.

#### 4.1. If Example1.

Consider the following C code:

```c
int main(){
	int a = -1, b = 2;
	if(a == b){
		return 1;
	}
	if(a > b){
		return 2;
	}
	if(a < b){
		return 3;
	}
	return 0xdefea7;
}
```

The code initialize two integers and the return value varies on several comparisons.

Thus, lets retrieve the assembly of this code, first from MCVS 2019:

```assen
0000000140001000 48 83 EC 18          sub         rsp,18h  
0000000140001004 C7 44 24 04 FF FF FF FF mov         dword ptr [a],0FFFFFFFFh 
000000014000100C C7 04 24 02 00 00 00 mov         dword ptr [rsp],2  
0000000140001013 8B 04 24             mov         eax,dword ptr [rsp] 		
0000000140001016 39 44 24 04          cmp         dword ptr [a],eax  
000000014000101A 75 07                jne         main+23h (0140001023h)  
000000014000101C B8 01 00 00 00       mov         eax,1  
0000000140001021 EB 25                jmp         main+48h (0140001048h)  
0000000140001023 8B 04 24             mov         eax,dword ptr [rsp]  
0000000140001026 39 44 24 04          cmp         dword ptr [a],eax  
000000014000102A 7E 07                jle         main+33h (0140001033h)  
000000014000102C B8 02 00 00 00       mov         eax,2  
0000000140001031 EB 15                jmp         main+48h (0140001048h)  
0000000140001033 8B 04 24             mov         eax,dword ptr [rsp]  
0000000140001036 39 44 24 04          cmp         dword ptr [a],eax  
000000014000103A 7D 07                jge         main+43h (0140001043h)  
000000014000103C B8 03 00 00 00       mov         eax,3  
0000000140001041 EB 05                jmp         main+48h (0140001048h)  
0000000140001043 B8 A7 FE DE 00       mov         eax,0DEFEA7h  
0000000140001048 48 83 C4 18          add         rsp,18h  
000000014000104C C3                   ret  
```

- First, it extends the stackframe to make space for the local variables.

	```assem
	sub         rsp,18h 
	```

- Then, assign the initialized local variables:

	```assem
	mov         dword ptr [a],0FFFFFFFFh  ; a = -1
	mov         dword ptr [rsp],2  ; 			b = 2
	```

- Now the compiler moves the 'b' local variable value to a register in order to operate with it and 'a', since is not allowed to compare (CMP) data accesing to memrory address at once in x86.

	```assem
	mov         eax,dword ptr [rsp]
	```
- Then comes the if statement. This is constituted with two instructions:

	1. First, the CMP instruction performs the substraction between the two values and modify the RFLAGS register bits.

	2. Then, depending of the specific comparison, a variant of JMP follows the CMP instruction, in this case, in C the if statement is evaluating if "a==b" so the JMP variant is JNE which checks if the ZF bit of the RFLAGS register is up. If it is jumps the target address which is the next CMP statement kit:

		```assem
		cmp         dword ptr [a],eax  
		jne         main+23h (0140001023h)
		```

		If not, it means that the comparison is true and simply enters the if block, this is, move into EAX the return value and jump to the RET instruction which would be the end of the code:

		```assem
		mov         eax,1  
		jmp         main+48h (0140001048h)
		```
		
- Then, it comes the following if-statement, note that the compiler moves again the rsp value to eax in a unoptimized compiler move:

	```assem
	mov         eax,dword ptr [rsp]  
	cmp         dword ptr [a],eax  
	jle         main+33h (0140001033h)  
	mov         eax,2  
	jmp         main+48h (0140001048h)
	```

	Note that the operation is barely the same buit this time, instead of use JNE, is using JLE which checks (ZF=1 || SF!=OF), this means; evaluates if the two values are equal or if, first, if the sign bit is up without an overflow being happened (SF=1, OF=0), second, if the result is positive with an overflow (SF=0, OF=1). Note that both cases means that b is greater than a; one because the substraction "a-b" is negative or two, because "a-b" is positive but overflowing, which means in fact is negative but it gets wrapped over positive due to hardware limitations.

	Note that always the if-statement is checking the opposite event: a > b; a greater than b. By default the flow execution prones to enter the if-block, only if this is false, jumps to another part. 

- Lastly, the last if statement which is pretty the same of the two cases above:

	```assem
	mov         eax,dword ptr [rsp]  
	cmp         dword ptr [a],eax  
	jge         main+43h (0140001043h)  
	mov         eax,3  
	jmp         main+48h (0140001048h)
	```

Thus, the logic of an if-statement in assembly is to implement first a comparison with CMP instruction and set the bits of RFLAGS register, then implements a variant of JMP instruction that evaluates if the if condition is false and it is skip the if block code (is not, it just enters).

<br>

Let's check the same C code compiled with GCC and extracted with radare2:

```assem
$ r2 -e asm.sub.var=false -A -qc "aaa; s main;pdf" test
Warning: run r2 with -e bin.cache=true to fix relocations in disassembly
            ; DATA XREF from entry0 @ 0x1058
┌ 74: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_8h @ rbp-0x8
│           ; var signed int var_4h @ rbp-0x4
│           0x00001129      f30f1efa       endbr64
│           0x0000112d      55             push rbp
│           0x0000112e      4889e5         mov rbp, rsp
│           0x00001131      c745f8ffffff.  mov dword [rbp - 8], 0xffffffff ; -1
│           0x00001138      c745fc020000.  mov dword [rbp - 4], 2
│           0x0000113f      8b45f8         mov eax, dword [rbp - 8]
│           0x00001142      3b45fc         cmp eax, dword [rbp - 4]
│       ┌─< 0x00001145      7507           jne 0x114e
│       │   0x00001147      b801000000     mov eax, 1
│      ┌──< 0x0000114c      eb23           jmp 0x1171
│      ││   ; CODE XREF from main @ 0x1145
│      │└─> 0x0000114e      8b45f8         mov eax, dword [rbp - 8]
│      │    0x00001151      3b45fc         cmp eax, dword [rbp - 4]
│      │┌─< 0x00001154      7e07           jle 0x115d
│      ││   0x00001156      b802000000     mov eax, 2
│     ┌───< 0x0000115b      eb14           jmp 0x1171
│     │││   ; CODE XREF from main @ 0x1154
│     ││└─> 0x0000115d      8b45f8         mov eax, dword [rbp - 8]
│     ││    0x00001160      3b45fc         cmp eax, dword [rbp - 4]
│     ││┌─< 0x00001163      7d07           jge 0x116c
│     │││   0x00001165      b803000000     mov eax, 3
│    ┌────< 0x0000116a      eb05           jmp 0x1171
│    ││││   ; CODE XREF from main @ 0x1163
│    │││└─> 0x0000116c      b8a7fede00     mov eax, 0xdefea7
│    │││    ; CODE XREFS from main @ 0x114c, 0x115b, 0x116a
│    └└└──> 0x00001171      5d             pop rbp
└           0x00001172      c3             ret
```

We can see that this time the code is barely the same, introduce the data in the local variables and start comparing the code with the same structure than the code generated by MCSV 2019, the if-statement are the composition of two instructions CMP (which evaluates the substraction of the two operands) and a variant of JMP instruction, which depends of the operation performed by the if condition and evalutes the opposite condition. If is true skip the if block if not, continues and enters the if-block code.
 
<br>

#### 4.2. If example2.

Consider the following C code:

```c
int main(){
	unsigned int a = -1, b = 2;
	if(a == b){
		return 1;
	}
	if(a > b){
		return 2;
	}
	if(a < b){
		return 3;
	}
	return 0xdefea7;
}
```

The only difference between this code and the code above is the intergers variables are now unsigned, the dissasembly of MCSV 2019

```assem
0000000140001000 48 83 EC 18          sub         rsp,18h  
0000000140001004 C7 44 24 04 FF FF FF FF mov         dword ptr [a],0FFFFFFFFh  
000000014000100C C7 04 24 02 00 00 00 mov         dword ptr [rsp],2  
0000000140001013 8B 04 24             mov         eax,dword ptr [rsp]  
0000000140001016 39 44 24 04          cmp         dword ptr [a],eax  
000000014000101A 75 07                jne         main+23h (0140001023h)  
000000014000101C B8 01 00 00 00       mov         eax,1  
0000000140001021 EB 25                jmp         main+48h (0140001048h)  
0000000140001023 8B 04 24             mov         eax,dword ptr [rsp]  
0000000140001026 39 44 24 04          cmp         dword ptr [a],eax  
000000014000102A 76 07                jbe         main+33h (0140001033h)  
000000014000102C B8 02 00 00 00       mov         eax,2  
0000000140001031 EB 15                jmp         main+48h (0140001048h)  
0000000140001033 8B 04 24             mov         eax,dword ptr [rsp]  
0000000140001036 39 44 24 04          cmp         dword ptr [a],eax  
000000014000103A 73 07                jae         main+43h (0140001043h)  
000000014000103C B8 03 00 00 00       mov         eax,3  
0000000140001041 EB 05                jmp         main+48h (0140001048h)  
0000000140001043 B8 ED A7 FE DE       mov         eax,0DEFEA7EDh  
0000000140001048 48 83 C4 18          add         rsp,18h  
000000014000104C C3                   ret 
```

Let's observe that, despite the if-statements are the same than in the other code, the JMP variants are differents. This means that the compilers generates code based on the datatype written by the user. The choice of conditional jump instruction (JA/JB/JAE/JBE for unsigned vs. JG/JL/JGE/JLE for signed) reveals the original variable's signedness—useful for reconstructing type information when analyzing binaries.

In the other hand; It turns out that for instructions that set status flags (e.g. arithmetic operations), the hardware just does the operation and sets flags as if the operands were both unsigned and signed. Basically the hardware doesn't know or care about whether the humans are currently interpreting the bits as signed or unsigned. That's the compiler's problem to sort out.

<br>

#### 4.3. Switch Example.

Consider the following C code:

```c
#include <stdlib.h>
int main(int argc, char* argv[]) {
    int a = atoi(argv[1]);
    switch (a) {
    case 0:
        return 1;
    case 1:
        return 2;
    default:
        return 3;
    }
    return 0xfee1fed;
}
```

In this case, we have a SWITCH directive that evaluates the input that the user-provides through the cli-parameter and provides three cases.

The dissasembly shows that the compiler treats the switch directive as if were a bunch of if-statements:

```assem
0000000140001000 48 89 54 24 10       mov         qword ptr [rsp+10h],rdx  
0000000140001005 89 4C 24 08          mov         dword ptr [rsp+8],ecx  
0000000140001009 48 83 EC 38          sub         rsp,38h  
000000014000100D B8 08 00 00 00       mov         eax,8  
0000000140001012 48 6B C0 01          imul        rax,rax,1  
0000000140001016 48 8B 4C 24 48       mov         rcx,qword ptr [argv]  
000000014000101B 48 8B 0C 01          mov         rcx,qword ptr [rcx+rax]  
000000014000101F FF 15 53 31 00 00    call        qword ptr [__imp_atoi (0140004178h)]  
0000000140001025 89 44 24 24          mov         dword ptr [a],eax  
0000000140001029 8B 44 24 24          mov         eax,dword ptr [a]  
000000014000102D 89 44 24 20          mov         dword ptr [rsp+20h],eax  
0000000140001031 83 7C 24 20 00       cmp         dword ptr [rsp+20h],0  
0000000140001036 74 09                je          main+41h (0140001041h)  
0000000140001038 83 7C 24 20 01       cmp         dword ptr [rsp+20h],1  
000000014000103D 74 09                je          main+48h (0140001048h)  
000000014000103F EB 0E                jmp         main+4Fh (014000104Fh)  
0000000140001041 B8 01 00 00 00       mov         eax,1  
0000000140001046 EB 13                jmp         main+5Bh (014000105Bh)  
0000000140001048 B8 02 00 00 00       mov         eax,2  
000000014000104D EB 0C                jmp         main+5Bh (014000105Bh)  
000000014000104F B8 03 00 00 00       mov         eax,3  
0000000140001054 EB 05                jmp         main+5Bh (014000105Bh)  
0000000140001056 B8 ED 1F EE 0F       mov         eax,0FEE1FEDh  
000000014000105B 48 83 C4 38          add         rsp,38h  
000000014000105F C3                   ret 
```

It is worth to note that this code is compiled and extracted in MCVS 2019 and follows Microsoft x64 ABI standards, thus, is worth to break down the first instructions:

- First, is setting the argc and argv arguments which come from RCX and RDX (standard in ABI convention). This is possible due to the shadow space alloced by the caller of main.

```assem
mov         qword ptr [rsp+10h],rdx  
mov         dword ptr [rsp+8],ecx 
```

- Then, it allocates the shadow space for the atoi() function:

```assem
sub         rsp,38h 
```

- Lastly, it introduces in RCX the argument of atoi() which is argv[1]:

```assem
000000014000100D B8 08 00 00 00       mov         eax,8  
0000000140001012 48 6B C0 01          imul        rax,rax,1  
0000000140001016 48 8B 4C 24 48       mov         rcx,qword ptr [argv]  
000000014000101B 48 8B 0C 01          mov         rcx,qword ptr [rcx+rax]  
```

	Note that, is a convoluted way to introduce the word size (in x64, which is the size of a pointer) into RAX and then add it to the argv pointer, the result is in terms of pointer arithmetics, argv + 1 or argv[1] being stored in RCX


<br>
