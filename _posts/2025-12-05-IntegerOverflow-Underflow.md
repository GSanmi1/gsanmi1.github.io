---
layout: post
title: "Integer Overflow/Underflow."
subtitle: "Notes from Integer Overflow course from OST2."
date: 2025-12-05 09:00:00 +0000
categories: ['Past Blogs', 'Binary Exploitation']
tags: ['memory-corruption', 'exploits']
author: German Sanmi
---


### 1. Integer Overflow/Underflow vulnerabilities introduction.

Integer Overflow/Undwerflow vulnerabilities referer a vulnerability form in which an attacker leverage cases in which is possible that signed and unsigned integers exceeds their positive and negative value ranges due to egdy math cases.

Before enter in a further explanation, let's take a reminder on how signed and unsigned data types works in C.

<br>

#### 1.1. Values and Datatypes.

**Value and Datatypes definition**

Let's start in the beginning, building the idea of *value* and *datatype*.

- A *value* is nothing but an abstraction of a piece of information stored in memory in form of binary bits waiting to be processed by the CPU.

- A *datatype* tells the compiler how to interpret and store that value in memory. It defines two critical things:

    1. The size of the value; this is *how many bytes to allocate*; (char, short, integer, ..., array, struct,...).

    2. The sign of the value; or *how to interpret the bit pattern stored there* (signed/unsigned). The same bit pattern 0xFF could mean 255 or -1 depending on how the compiler interprets it. 

<br>

**Signed vs Unsigned**

The sign of a value is also related with the datatype it self, because there are datatypes in which make a signed/unsigned distinction does not make sense. *The signed/unsigned distinction only applies to integer types* (char, short, int, long, etc.) because it's about how to interpret a fixed sequence of bits as a number. Floating-point types, structs, pointers does not have an unsigned version.

- *Unsigned integers* use all bits to represent magnitude. An 8-bit unsigned value ranges from 0 to 255 (2⁸ - 1). Every bit pattern maps directly to a non-negative number.

- *Signed integers* uses the most significant bit to encode sign information, is called the sign bit. Using two's complement representation (which is universal on modern systems), an 8-bit signed value ranges from -128 to 127. The bit pattern 0xFF becomes -1 rather than 255.

<br>

#### 1.2. Two's Complement Signed Numbers.

Two's complement is the standard way that C (and most modern computers) represents signed integers (positive and negative whole numbers).

In this representation, the leftmost (or more significant bit) serves also as an indicator to notice the sign of the value:

- '0' to positive numbers; 01111111b = 127
- '1' to negative numbers. 10000000b = -128

Thus, let's suppose we have a binary number, lets say *x*, the complement's convention says that in order to represent *-x* we have to flip all the bits (0→1, 1→0) this is called the one's complement and then add 1:

```
Positive number: 5

- 00000101b 

Negative number: -5

- Step 1: Start with 5:     00000101
- Step 2: Flip all bits:     11111010  (one's complement)
- Step 3: Add 1:             11111011  = -5 (two's complement)
```

The formula to obtain the decimal value from a signed integer binary number is applying a negative sign to sign bit in the standard base system operation, for example:

```
11111011 = -1*2^7 + 1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = -128 + 64 + 32 + 16 + 8 + 0 + 2 + 1 = -128 + 123 = -5
```

<br>

#### 1.3. Range of a datatype.

A word about the range. A *range* is simply the set of all possible values a datatype can represent and is not an arbitrary decision but a direct consequence of having finite storage capacity. Memory is organized into units of 8-bits each (also called byte), and CPUs have registers of fixed widths: 8, 16, 32, or 64 bits on modern systems. This means that, often, you only have at most 64 bits (possibles 0 or 1) to store a binary value which represents data, this also means that every datatype has a finite range.

For signed integers, the absolute value decrements in a half compared with the unsigned type and, for example, to a 8 bits value, the maximum unsigned value is 11111111b, which in decimal is 255. But, for the signed type, by convention, since the leftmost bit is consider the sign bit, then the further value from zero is 1111111b = 127. 

It happens that:

```
n-bit signed integer --> the range is: -2^(n-1) to 2^(n-1) - 1
```

<br>

| binary     | hex | unsigned decimal | signed decimal |
|------------|-----|------------------|----------------|
| 00000000   | 00  | 0                | 0              |
| 00000001   | 01  | 1                | 1              |
| 00000010   | 02  | 2                | 2              |
| 00000011   | 03  | 3                | 3              |
| ...        | ... | ...              | ...            |
| 01111110   | 7E  | 126              | 126            |
| 01111111   | 7F  | 127              | 127            |
| 10000000   | 80  | 128              | -128           |
| 10000001   | 81  | 129              | -127           |
| ...        | ... | ...              | ...            |
| 11111110   | FE  | 254              | -2             |
| 11111111   | FF  | 255              | -1             |

<br>

This exact principle showed with 8-bits can be extended also to 16,32 and 64 bits numbers:

- 8-bit signed (char): -128 to 127
- 16-bit signed (short): -32,768 to 32,767
- 32-bit signed (int): -2,147,483,648 to 2,147,483,647


<br>

### 2. Integer Overflow Definition.

At this moment, with the having introduced the previous terms, we are now in conditions to provide a definition.

<br>

#### 2.1. Unsigned Overflow/Underflow.

Let's consider the following trivial code:

```c
unsigned char i = 0;
while(1) i++;
```

In the code above, an unsigned char gets defined with value 0 and then a while loop starts increasing the value of *i* once at a time.

As de loops iterates, i value increases but since char size is one byte, it only can store 8-bits, so eventually:


| iteration |  uchar (binary) | uchar (hex) | uchar (decimal) |
| - | - | - | - |
| ... | ... | ... | ... |
| 254 | 11111110 | FE | 254 |
| 255 | 11111111 | FF | 255 (Upper-top range) | 
| 256 | 1(00000000) | 1(00) | 0 |
| 257 | 000000001 | 01 | 1 |
| ... | ... | ... | ... |


What is happenning is that the CPU is perfoming the correct calculation which is 11111111 + 1 = 100000000 (a 9-bit value) and is storing it in a 8-bit size chunk, so as the result, the most significant bit is left out and what is stored at the chunk is the value 00000000, restarting the value of *i*. This is what we call *Unsigned Overflow*.

This can be resumed as the following rule: **All the operations performed over an unsigned datatype are modular operations with module 2^N where N is the bit-width of the type**.

*Unsigned overflow* is well-defined in C. The standard explicitly says unsigned arithmetic wraps modulo 2^n. If you add 1 to UINT_MAX, you get 0. This is guaranteed, portable behavior. The opposite case, going behind 0 to obtain instantetly the biggest value posible is what we call *Signed Underflow*.


<br>

#### 2.2. Signed Overflow/Underflow.

Signed Integers, as discussed before, have a different design than unsigned datatypes. Since both entities are confined within a finite storage capacity both share range boundaries and the overflow type related to the range boundaries discussed above.

But signed integers also leads to another type of overflow dealing with the change of sign. Let's start saying negativity is a decimal-level abstraction. At the binary level, you just have rings of integers mod 2^n, and two's complement is the isomorphism that maps the upper half of that ring onto negative numbers in a way that preserves additive structure.

Lets dive on how this isomorphism works. By definition, if we have a value 'x' in a set o numbers, his negative is that number in the set which add to 0 with 'x':

```
x + (-x) = 0
```

Let's consider a binary value of 8-bit wide, 00000011 (3) if we calculate the negative through the two's complement: 

```
x = 1 --> -x = 11111110 + 1 = 11111111 = 255
x = 2 --> -x = 11111101 + 1 = 11111110 = 254
x = 3 --> -x = 11111100 + 1 = 11111101 = 253
x = 4 --> -x = 11111011 + 1 = 11111100 = 252
...
```

We can see a clear pattern, as we go on the values from the lower limit of the range (0), his negative correspondient value is the homologous value startint from te upper limit (256) and the flow of both values advance to opposite directions so they are meant to encounter each other at the half of the track.

```
x = 126 --> -x = 10000001 + 1 = 10000010 = 130
x = 127 --> -x = 10000000 + 1 = 10000001 = 129
x = 128 --> -x = 01111111 + 1 = 10000000 = 128 <-- Inflection point
x = 129 --> -x = 01111110 + 1 = 01111111 = 127
x = 130 --> -x = 01111101 + 1 = 01111110 = 126
```

Thus, we can assume the convention that from 127 all the numbers above are the negative counter part of the half below 127.

<br>

| binary     | unsigned decimal | signed decimal |
|------------|------------------|----------------|
| 00000000   | 0                | 0              |
| 00000001   | 1                | 1              |
| 00000010   | 2                | 2              |
| 00000011   | 3                | 3              |
| ...        | ...              | ...            |
| 01111110   | 126              | 126            |
| 01111111   | 127              | 127            |
| 10000000   | 128              | -128           |
| 10000001   | 129              | -127           |
| ...        |  ...             | ...            |
| 11111110   | 254              | -2             |
| 11111111   | 255              | -1             |

<br>

Thus, in any modular 2^N ring the values increases until some threshold is reached (the half of the ring) and then the value goes from being the highest value to the smallest one, this is what we call *Signed Overflow*. The opposite case, when the values decreases until goes from the smallest value to the highest one is called *Signed Underflow*. Signed overflow is undefined behavior in C. The standard says the compiler can assume it never happens, which means if your code allows it to happen, the compiler is free to do anything: wrap around, saturate, crash, optimize away your bounds check, or summon demons. In practice, most compilers on most platforms will wrap using two's complement (so INT_MAX + 1 becomes INT_MIN).

Let's note again that negativity is just a convention, we explain how positive and negative values are relate between them using the 'negative' and two's complement definitions only in behalf of clarity. Negative and substraction are concepts tightly related and is easier to think about them because we are made to an infinite set of numbers. In fact, in modular rings as 8-bit width binary values negativness is a direct consecuence of the modular nature of the ring:

```
127 + (-127) = 01111111 + 10000001 = 1(00000000)
```

Also the risk of this effect and the reason why this leads into a vulnerability is also a consecuence of the modular nature of the set of numbers.

<br>

#### 2.3. Conclusion and explaning the risk.

Integer overflows shows them selfs as vulnerabilties due to "under-allocation" and "over-copy", for examples:

```c
//Assume var is user-controlled
malloc(var1 + const)
malloc(var1 + var2)
malloc(var1 * const)
```

All of this allocations present issues of having underallocation.

If again this number is used to copy data with checking the memory chunk allocated:

```c
memcpy(dst, src, var1)
```

This can be an over-copy.

<br>

### 3. Examples.

#### 3.1. Trivial Example:

Let's check the following code.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct my_header{
    unsigned long int magic;
    unsigned long int size;
} my_header_t;

// Under-allocate, over-copy – uaoc.c
void main(int argc, char *argv[]){
    my_header_t header;
    unsigned int alloc_size;

    header.magic = 0x6f6e6558;
    header.size  = strtoul(argv[1], NULL, 10);
    alloc_size   = header.size + sizeof(my_header_t);

    printf("String self-reported size = 0x%08lX\n", header.size);
    printf("Allocation size = 0x%08X\n", alloc_size);

    char *buf = malloc(alloc_size);
    if(buf == NULL) return;

    printf("buf points to %p\n", buf);

    memcpy(buf, &header, sizeof(my_header_t));
    buf += sizeof(my_header_t);

    printf("memcpy()ing 0x%08lX bytes into buf of size 0x%08X\n",
           header.size, alloc_size);

    memcpy(buf, argv[2], header.size);

    printf("We copied input string: %s\n", buf);
}
```

If we check the code, we can see that some user-controlled data *argv\[1\}* is being stored on *size* field of *header* struct and inmediately without sanitization, this same value is used to allocate memory space:

```c
header.size  = strtoul(argv[1], NULL, 16);
alloc_size   = header.size + sizeof(my_header_t);
//...
char *buf = malloc(alloc_size);
```

Thus, let's observe that, since *header.size* is arbitrary and *my_header_t* struct have two fields (two longs), *then sizeof(my_header_t)* in x64 is 16 bytes and the unsigned int in x64 has 4 bytes in size, so is a value within a range between 0 and 2^(4*8) = 2^32 (4 bytes, 8 bits each byte) = 4294967296, thus if the user enters 4294967280 (4294967296 - 16) *alloc_size* would be overflow an turn 0, this means that this code can easily turns into an underallocation.

Later, the pointer is used as a destination in a *memcpy()* operation:

```c
memcpy(buf, argv[2], header.size);
```

The reuslt is overcopying:

```less
OUTPUT:
$ ./test 4294967280 hello
String self-reported size = 0xFFFFFFF0
Allocation size = 0x00000000
buf points to 0x58449e0336b0
memcpy()ing 0xFFFFFFF0 bytes into buf of size 0x00000000
Segmentation fault (core dumped)
```

<br>

#### 3.2. FreeRTOS.

Lets consider the following code:

```c
void pvPortMalloc( size_t xWantedSize ) {v//user-controlled - xWantedSize 
    BlockLink_t *pxBlock, *pxPreviousBlock, *pxNewBlockLink;
    static BaseType_t xHeapHasBeenInitialised = pdFALSE;
    void *pvReturn = NULL;

    vTaskSuspendAll();
    {
        /* If this is the first call to malloc then the heap
         * initialisation to setup the list of free blocks. */
        if( xHeapHasBeenInitialised == pdFALSE )
        {
            prvHeapInit();
            xHeapHasBeenInitialised = pdTRUE;
        }

        /* The wanted size is increased so it can contain a BlockLink_t
         * structure in addition to the requested amount of bytes. */
        if( xWantedSize > 0 )
        {
            xWantedSize += heapSTRUCT_SIZE;

            /* Ensure that blocks are always aligned to the required number of bytes. */
            if( ( xWantedSize & portBYTE_ALIGNMENT_MASK ) != 0 )
            {
                /* Byte alignment required. */
                xWantedSize += ( portBYTE_ALIGNMENT - ( xWantedSize & portBYTE_ALIGNMENT_MASK ) );
            }
        }
    }
}
```

We can see that *xWantedSize*, which is a *size_t* datatype (unsigned integer) is user-controlled and used within an if statement performing a math operation with *heapSTRUCT_SIZE* without validation, thus as we proceed in the case before, we could perform an unsigned overflow.

<br>

### 4. Exercises.

#### 4.1. CVE-2020-0796 "SMBGhost".

CVE-2020-0796, commonly known as SMBGhost, is a critical remote code execution vulnerability discovered in March 2020 that affects Microsoft's SMBv3 (Server Message Block version 3) protocol implementation in Windows 10 and Windows Server versions 1903 and later.

SMB3 supports message compression to reduce network traffic load, message decompression takes place in the srv2.sys kernel driver.

<br>

```c
////ACID: The data pointed to by request->pNetRawBuffer
signed __int64 __fastcall Srv2DecompressData(SRV2_WORKITEM *workitem)
{
    // declarations omitted
    ...
    request = workitem->psbhRequest;
    if ( request->dwMsgSize < 0x10 )
        return 0xC000090B;
    compressHeader = *(CompressionTransformHeader *)request->pNetRawBuffer;
    ...
   
    newHeader = SrvNetAllocateBuffer((unsigned int)(compressHeader.originalCompressedSegSize + compressHeader.offsetOrLength), 0);
    if ( !newHeader )
        return 0xC000009A;
   
    if ( SmbCompressionDecompress(
                compressHeader.compressionType,
                &workitem->psbhRequest->pNetRawBuffer[compressHeader.offsetOrLength + 16],
                workitem->psbhRequest->dwMsgSize - compressHeader.offsetOrLength - 16,
                &newHeader->pNetRawBuffer[compressHeader.offsetOrLength],
                compressHeader.OriginalCompressedSegSize,
                &finalDecompressedSize) < 0
            || finalDecompressedSize != compressHeader.originalCompressedSegSize) )
    {
        SrvNetFreeBuffer(newHeader);
        return 0xC000090B;
    }
    if ( compressHeader.offsetOrLength )
    {
        memmove(newHeader->pNetRawBuffer, workitem->psbhRequest->pNetRawBuffer + 16, compressHeader.offsetOrLength);
    }
    newHeader->dwMsgSize = compressHeader.OffsetOrLength + fianlDecompressedSize;
    Srv2ReplaceReceiveBuffer(workitem, newHeader);
    return 0;
}
```

Then, let's go carefully, checking the code, the user controlled data is pointed by *request->pNetRawBuffer*, thus:

- First, *compressHeader* gets the dereferenced contents of *request->pNetRawBuffer*, then some fields of this structure gets used to allocate a buffer presumibly inside the heap:

    ```c
    compressHeader = *(CompressionTransformHeader *)request->pNetRawBuffer;
   
    newHeader = SrvNetAllocateBuffer((unsigned int)(compressHeader.originalCompressedSegSize + compressHeader.offsetOrLength), 0);
    ```

    This essentially could lead to an underallocation since no check is done after or before the allocation.


- Later, *offsetOrLength* field is used to copy memory to the previos allocated buffer which could lead to an overcopy:

    ```c
    if ( compressHeader.offsetOrLength ){
        memmove(newHeader->pNetRawBuffer, workitem->psbhRequest->pNetRawBuffer + 16, compressHeader.offsetOrLength);
    }
    ```

- As a summary, an addition of two user-controlled terms could be used to perform an underallocation due to an unsigned integer overflow, for example if *compressHeader.originalCompressedSegSize* is small and *compressHeader.offsetOrLength* was huge always being:

    ```c
    compressHeader.originalCompressedSegSize + compressHeader.offsetOrLength = 2^32
    ```

    Then, on the second line, a huge amountn of bytes would be used to write over an small buffer provoking an overcopy resulting in a bufffer overflow.

<br>

#### 4.2. CVE-2019-5105.

CVE-2019-5105 is a critical memory corruption vulnerability affecting 3S-Smart Software Solutions' CODESYS industrial automation platform, specifically in the GatewayService component. While primarily classified as an out-of-bounds write vulnerability, it's related to integer overflow issues in buffer size calculations.

```c

////ACID: param_1
void FUN_00677d70(void **param_1, int param_2, int param_3, int param_4, int param_5 ,uint *param_6)
{
  int header_length;
  size_t _Size;
  int iVar1;
  int iVar2;
  int receiver_length;
  uint sender_length;
  /* Omitted code  */
  void *blkDrvPDUdata;
  /* Omitted code */
  iVar2 = *(int *)(param_2 + 0x128) +  DAT_007a3534;
  if (iVar2 < 0xf) {
     /* Omitted code */
    blkDrvPDUdata = *param_1;
    header_length = (*(byte *)((int)blkDrvPDUdata + 1) & 7) * 2;
    sender_length = *(byte *)((int)blkDrvPDUdata + 5) & 0xf;
    receiver_length = (int)(uint)*(byte *)((int)blkDrvPDUdata + 5) >> 4;
    pvVar3 = (void *)(sender_length + receiver_length + header_length);
    local_20c = header_length;
    if (pvVar3 < param_1[1] || pvVar3 == param_1[1]) {
      pvVar3 = *param_1;
      if ((*(byte *)((int)blkDrvPDUdata + 2) & 0x10) == 0) {
        *param_6 = header_length + (sender_length + receiver_length) * 2;
        if ((*param_6 & 3) != 0) {
          *param_6 = *param_6 + 2;
        }
        _Size = (int)param_1[1] - *param_6;

        /* Omitted  code*/
        if ((local_220 < 0x10) && (local_244 < 0x10)) {      
          /* Omitted  Code*/              
          if (local_20c + _Size_00 + iVar1 + local_214 + _Size < 0x201) {
            memcpy(local_208 + local_214 + iVar1 + _Size_00 + local_20c, (void *)((int)*param_1 + *param_6), _Size );
            param_1[1] = (void *)(local_20c + _Size_00 + iVar1 + local_214 + _Size);
            memcpy(*param_1,local_208,(size_t)param_1[1]);
            *(int *)(param_5 + 0xc) = (int)*param_1 + local_20c;
            *(int *)(param_4 + 0xc) = *(int *)(param_5 + 0xc) + *(int *)(param_5 + 8) * 2;
            *param_6 = local_20c + _Size_00 + iVar1;
            if ((*param_6 & 3) != 0) {
              *param_6 = *param_6 + 2;
            }
          }
        }
      }
    }
  }
  FUN_006ce8f9();
  return;
}
```

Let's review the code carefully, user-controlled data lies on *param_1*.

- First, some declaration are perfomed:

    ```c
    int header_length;
    size_t _Size;
    int iVar1;
    int iVar2;
    int receiver_length;
    uint sender_length;
    /* Omitted code  */
    void *blkDrvPDUdata;
    /* Omitted code */
    iVar2 = *(int *)(param_2 + 0x128) +  DAT_007a3534;
    //...
    ```

- Then, comes the assignation, in which some variables in the function receives user-controlled data:

    ```c
    blkDrvPDUdata = *param_1;
    header_length = (*(byte *)((int)blkDrvPDUdata + 1) & 7) * 2;
    sender_length = *(byte *)((int)blkDrvPDUdata + 5) & 0xf;
    receiver_length = (int)(uint)*(byte *)((int)blkDrvPDUdata + 5) >> 4;
    pvVar3 = (void *)(sender_length + receiver_length + header_length);
    local_20c = header_length;
    ```

    Essentially, is not hard to see that all of this variables are user-controlled

- Now, this variables are used to define the copy size, the source and the destination of a memcpy() operation:

    ```c
    *param_6 = header_length + (sender_length + receiver_length) * 2; //User-controlled
    //...
    _Size = (int)param_1[1] - *param_6; //Underflow
    //...
    memcpy(local_208 + local_214 + iVar1 + _Size_00 + local_20c, (void *)((int)*param_1 + *param_6), _Size ); //Overcopy
    param_1[1] = (void *)(local_20c + _Size_00 + iVar1 + local_214 + _Size);
    memcpy(*param_1,local_208,(size_t)param_1[1]);
    ```

    Let's observe carefully that when _Size filled, if  *\*param_6* > than *(int)param_1\[1\]* then, it could result in a negative value that, when cast to unsigned it will transform in a huge positive value leading to an overcopy

<br>

#### 4.3. CVE-2019-14192.

CVE-2019-14192 is an integer overflow vulnerability discovered in U-Boot (Universal Boot Loader), which is one of the most widely used boot loaders for embedded systems. 

Firmware fetch the bootloader which in this case is u-boot and this devices loads the OS and this one the rest of the applications.

Let's check the code:

```c
////ACID: in_packet
void net_process_received_packet(uchar *in_packet, int len) {
	struct ethernet_hdr *et;
	struct ip_udp_hdr *ip;
	struct in_addr dst_ip;
	struct in_addr src_ip;
	int eth_proto;
	// ...
	ip = (struct ip_udp_hdr *)(in_packet + E802_HDR_SIZE);
	// ...
	switch (eth_proto) {
	// ...
	case PROT_IP:
		debug_cond(DEBUG_NET_PKT, "Got IP\n");
		/* Before we start poking the header, make sure it is there */
		if (len < IP_UDP_HDR_SIZE) {
			debug("len bad %d < %lu\n", len, (ulong)IP_UDP_HDR_SIZE);
			return;
		}
		/* Check the packet length */
		if (len < ntohs(ip->ip_len)) {
			debug("len bad %d < %d\n", len, ntohs(ip->ip_len));
			return;
		}
		len = ntohs(ip->ip_len);
		// ...
		ip = net_defragment(ip, &len);
		if (!ip)
			return;
		// ...
		if (ip->ip_p == IPPROTO_ICMP) {
			receive_icmp(ip, len, src_ip, et);
			return;
		} else if (ip->ip_p != IPPROTO_UDP) {	/* Only UDP packets */
			return;
		}

		// ...
#if defined(CONFIG_NETCONSOLE) && !defined(CONFIG_SPL_BUILD)
		nc_input_packet((uchar *)ip + IP_UDP_HDR_SIZE, src_ip, ntohs(ip->udp_dst), ntohs(ip->udp_src), ntohs(ip->udp_len) - UDP_HDR_SIZE);
#endif
		/*
		 * IP header OK.  Pass the packet to the current handler.
		 */
		(*udp_packet_handler)((uchar *)ip + IP_UDP_HDR_SIZE, ntohs(ip->udp_dst), src_ip, ntohs(ip->udp_src), ntohs(ip->udp_len) - UDP_HDR_SIZE);
		break;
		// ...
	}
}
```

Let's note the following line:

```c
//...
ip = (struct ip_udp_hdr *)(in_packet + E802_HDR_SIZE);
//...
#if defined(CONFIG_NETCONSOLE) && !defined(CONFIG_SPL_BUILD)
		nc_input_packet((uchar *)ip + IP_UDP_HDR_SIZE, src_ip, ntohs(ip->udp_dst), ntohs(ip->udp_src), ntohs(ip->udp_len) - UDP_HDR_SIZE);
#endif
```

We can see that, the last parameter of the calling of *nc_input_packet()* function is math operation without validation of any type. We don't need to understand what the function does with that value in order to be able to see that is dangerous and is in fact a vulnerbility.

The same is done just below in the code:

```c
/*
    * IP header OK.  Pass the packet to the current handler.
    */
(*udp_packet_handler)((uchar *)ip + IP_UDP_HDR_SIZE, ntohs(ip->udp_dst), src_ip, ntohs(ip->udp_src), ntohs(ip->udp_len) - UDP_HDR_SIZE);
break;
// ...
```

A function is being called thorugh a function pointer and the last parameter is also a math operation without any validation.

(This is not in fact so dangerous as it seems, perhaps the function holds some validation for edgy values?)

<br>

#### 4.4. CVE-2020-11901. Part of "Ripple20" grab-bag.

CVE-2020-11901 is really 4 vulnerabilities that got lumped into the same CVE (/ didn’t get assigned their own CVEs), this was discussed before on Linear Stack Buffer Overflow.

This pertains to the parsing of compressed DNS packets. DNS packets have a formatting for hostname strings that breaks them into “labels”, that are prefixed by a label length byte. Multiple labels are separated by a period, the total hostname string is considered complete when a 0 is found for a label length. The DNS spec states that the max label length should be 63 bytes and the hostname length should be 255 bytes.

Consider the following code:

```c
//ACID: RDLENGTH, resourceRecordAfterNamePtr, dnsHeaderPtr
if (RDLENGTH <= remaining_size) {
	/* compute the next resource record pointer based on the RDLENGTH */
	labelEndPtr = resourceRecordAfterNamePtr + 10 + RDLENGTH;
	/* type: MX */
	if (cacheEntryQueryType == DNS_TYPE_MX && rrtype == DNS_TYPE_MX) {
		addr_info = tfDnsAllocAddrInfo();
		if (addr_info != NULL && RDLENGTH >= 2) {
			/* copy preference value of MX record */
			memcpy(&addr_info->ai_mxpref,resourceRecordAfterNamePtr + 10, 2);
			/* compute the length of the MX hostname */
			labelLength = tfDnsExpLabelLength(resourceRecordAfterNamePtr + 0xc, dnsHeaderPtr, labelEndPtr);
			addr_info->ai_mxhostname = NULL;
			if (labelLength != 0) {
				/* allocate buffer for the expanded name */
				asciiPtr = tfGetRawBuffer((uint)labelLength);
				addr_info->ai_mxhostname = asciiPtr;
				if (asciiPtr != NULL) {
					/* copy MX hostname to `asciiPtr` as ASCII */
					tfDnsLabelToAscii(resourceRecordAfterNamePtr + 0xc, asciiPtr, dnsHeaderPtr, 1, 0);
					/* ... */
				}
				/* ... */
			}
			/* ... */
		}
	/* ... */
	}
}

tt16Bit tfDnsExpLabelLength(tt8BitPtr labelPtr, tt8BitPtr pktDataPtr, tt8BitPtr labelEndPtr){
	tt8Bit currLabelLength;
	tt16Bit i = 0, totalLength = 0;
	tt8BitPtr newLabelPtr;

	while (&labelPtr[i] < labelEndPtr && labelPtr[i] != 0) {
		currLabelLength = labelPtr[i];
		if ((currLabelLength & 0xc0) == 0) {
			totalLength += currLabelLength + 1;
			i += currLabelLength + 1;
		} else {
			if (&labelPtr[i+1] < labelEndPtr) {
				newLabelPtr = pktDataPtr + (((currLabelLength & 0x3f) << 8) | labelPtr[i+1]);
				if (newLabelPtr < labelPtr) {
					labelPtr = newLabelPtr;
					i = 0;
					continue;
				}
			}
		return 0;
		}
	}
	return totalLength;
}
```

First of all, we understand by the name that *resourceRecordAfterNamePtr* and *dnsHeaderPtr* are both pointers and that *RDLENGTH* since is a length is most likely an unsigned integer.

Then, *labelEndPtr* pointer gets formed by adding to *resourceRecordAfterNamePtr* the term *10 + RDLENGTH*:

```c
labelEndPtr = resourceRecordAfterNamePtr + 10 + RDLENGTH;
```

Then, below, *tfDnsExpLabelLength()* is called with *resourceRecordAfterNamePtr + 0xc, dnsHeaderPtr, labelEndPtr* parameters, all user-controlled.

If we look closer at this code we can see that first memory access from *labelPtr* (which is user-controlled) is being performed and stored in *currLabelLength*:

```
currLabelLength = labelPtr[i];
```

And then several additions are done to create the value *totalLength*. Since this operations have no validations and there can as many labels as user wants (or said in other words, labelEndPtr is user-controlled and there can be as many iterations as user wants), an integer overflow can be done, returning small *totalLength* value.

This value is returned in *labelLength* which is used to allocate memory for a buffer:

```c
/* allocate buffer for the expanded name */
asciiPtr = tfGetRawBuffer((uint)labelLength);
```

Thus, the integer overflow can result in a underallocation which later in *tfDnsLabelToAscii* results in an overcopying vulnerability o buffer overflows.

<br>

#### 4.5. CVE-2020-16225.

Consider the following code:

```c

////ACID: The data read from staFileHandler
FILE *staFileHandler; //File handler is valid and already points to 0x200 location 
                      //in .sta file being loaded.
size_t x;
size_t y;
size_t allocSize;
void *memoryAllocation;

fread(&x, 4, 1, staFileHandler);
fread(&y, 4, 1, staFileHandler);
allocSize = y - x;
memoryAllocation = VirtualAlloc(0, allocSize, 0x3000, 4);
fread(memoryAllocation + x, 1, allocSize, staFileHandler);
```

Without validation of any type, allocsize is the substraction between two unsigned integer. This can lead to an integer underflow; A huge allocSize value which leads into a huge allocation which later can resultn in an overreading due to the fact that fread() is dumping allocSize bytes from staFileHandler into *memoryAllocation + x* which is also partially user-controlled.

<br>

#### 4.6. CVE-2020-17443.

picoTCP is a lightweight TCP/IP stack designed for embedded systems and IoT devices. The vulnerability exists in the DNS response parsing code, specifically in how the stack handles DNS name compression pointers.

When parsing DNS responses, picoTCP decompresses domain names that use DNS compression (the 0xC0 pointer mechanism). The flaw occurs during length calculation for the decompressed name.

Let's check the code:

```c
////ACID: echo
static int pico_icmp6_send_echoreply(struct pico_frame *echo)
{
    struct pico_frame *reply = NULL;
    struct pico_icmp6_hdr *ehdr = NULL, *rhdr = NULL;
    struct pico_ip6 src;
    struct pico_ip6 dst;

    reply = pico_proto_ipv6.alloc(&pico_proto_ipv6, echo->dev, (uint16_t)(echo->transport_len));
    if (!reply) {
        pico_err = PICO_ERR_ENOMEM;
        return -1;
    }

    echo->payload = echo->transport_hdr + PICO_ICMP6HDR_ECHO_REQUEST_SIZE;
    reply->payload = reply->transport_hdr + PICO_ICMP6HDR_ECHO_REQUEST_SIZE;
    reply->payload_len = echo->transport_len;

    ehdr = (struct pico_icmp6_hdr *)echo->transport_hdr;
    rhdr = (struct pico_icmp6_hdr *)reply->transport_hdr;
    rhdr->type = PICO_ICMP6_ECHO_REPLY;
    rhdr->code = 0;
    rhdr->msg.info.echo_reply.id = ehdr->msg.info.echo_reply.id;
    rhdr->msg.info.echo_reply.seq = ehdr->msg.info.echo_request.seq;
    memcpy(reply->payload, echo->payload, (uint32_t)(echo->transport_len - PICO_ICMP6HDR_ECHO_REQUEST_SIZE));
    rhdr->crc = 0;
    rhdr->crc = short_be(pico_icmp6_checksum(reply));
    /* Get destination and source swapped */
    memcpy(dst.addr, ((struct pico_ipv6_hdr *)echo->net_hdr)->src.addr, PICO_SIZE_IP6);
    memcpy(src.addr, ((struct pico_ipv6_hdr *)echo->net_hdr)->dst.addr, PICO_SIZE_IP6);
    pico_ipv6_frame_push(reply, &src, &dst, PICO_PROTO_ICMP6, 0);
    return 0;
}

/* allocates an IPv6 packet without extension headers. If extension headers are needed,
 * include the len of the extension headers in the size parameter. Once a frame acquired
 * increment net_len and transport_hdr with the len of the extension headers, decrement
 * transport_len with this value.
 */
static struct pico_frame *pico_ipv6_alloc(struct pico_protocol *self, struct pico_device *dev, uint16_t size)
{
    struct pico_frame *f = NULL;

    IGNORE_PARAMETER(self);

    if (0) {}
#ifdef PICO_SUPPORT_6LOWPAN
    else if (PICO_DEV_IS_6LOWPAN(dev)) {
        f = pico_proto_6lowpan_ll.alloc(&pico_proto_6lowpan_ll, dev, (uint16_t)(size + PICO_SIZE_IP6HDR));
    }
#endif
    else {
#ifdef PICO_SUPPORT_ETH
        f = pico_proto_ethernet.alloc(&pico_proto_ethernet, dev, (uint16_t)(size + PICO_SIZE_IP6HDR));
#else
        f = pico_frame_alloc(size + PICO_SIZE_IP6HDR + PICO_SIZE_ETHHDR);
#endif
    }

    if (!f)
        return NULL;

    f->net_len = PICO_SIZE_IP6HDR;
    f->transport_hdr = f->net_hdr + PICO_SIZE_IP6HDR;
    f->transport_len = (uint16_t)size;

    /* Datalink size is accounted for in pico_datalink_send (link layer) */
    f->len =  (uint32_t)(size + PICO_SIZE_IP6HDR);

    return f;
}
```

Then, lets go part by part:

- After a few definitions and declarations:

    ```c 
    struct pico_frame *reply = NULL;
    struct pico_icmp6_hdr *ehdr = NULL, *rhdr = NULL;
    struct pico_ip6 src;
    struct pico_ip6 dst;
    ```

    Part of the echo contents are dumped on reply structure:

    ```c
    echo->payload = echo->transport_hdr + PICO_ICMP6HDR_ECHO_REQUEST_SIZE;
    reply->payload = reply->transport_hdr + PICO_ICMP6HDR_ECHO_REQUEST_SIZE;
    reply->payload_len = echo->transport_len;
    ```

    Thus, this data-piece are user-controlled, 

- Later on the code, and without any previous validation, a memcpy() operation is performed:

    ```c
    memcpy(reply->payload, echo->payload, (uint32_t)(echo->transport_len - PICO_ICMP6HDR_ECHO_REQUEST_SIZE));
    ```

    Observe that, destination, source and the size are essentially user controlled. Since the size is a mathematical operation (a substraction) between a user-controlled data and a constant, potentially leading to an underflow, since the value is casted as an unsigned integer, the underflow would result in basically in a huge value as the size to be copied.

    Thus, this is a what-where-write vulnerability.

<br>

#### 4.7. CVE-2021-30860 "FORCEDENTRY".

JBIG2 (Joint Bi-level Image Experts Group) is an image compression format. JBIG2 data streams can be embedded into PDF files. PDF files will be automatically processed when delivered to a Mac/iPhone via iMessages

Therefore this is suitable for "zero-click" exploits, where the victim doesn't need to do anything (like clicking on a file or link) in order to be exploited


Apple had recently introduced a new sandboxing measure ("BlastDoor") to process ACID in a more restricted environment... but it turns out PDF files were not sandboxed...

<br>

Lets check the code:

```c
enum JBIG2SegmentType {
    jbig2SegBitmap,
    jbig2SegSymbolDict,
    jbig2SegPatternDict,
    jbig2SegCodeTable
};

////ACID: refSegs, nRefSegs
void JBIG2Stream::readTextRegionSeg(unsigned int segNum, bool imm, bool lossless, unsigned int length, unsigned int *refSegs, unsigned int nRefSegs){
    JBIG2Segment *seg;
    std::vector codeTables;
    JBIG2SymbolDict *symbolDict;
    JBIG2Bitmap **syms;
    unsigned int huff;
    unsigned int numSyms, symCodeLen;
    unsigned int i, k, kk;

    // ...

    // get symbol dictionaries and tables
    numSyms = 0;
    for (i = 0; i < nRefSegs; ++i) {
        if ((seg = findSegment(refSegs[i]))) {
            if (seg->getType() == jbig2SegSymbolDict) {
                numSyms += ((JBIG2SymbolDict *)seg)->getSize();
            } else if (seg->getType() == jbig2SegCodeTable) {
                codeTables.push_back(seg);
            }
        } else {
            error(errSyntaxError, curStr->getPos(), "Invalid segment reference in JBIG2 text region");
            return;
        }
    }

    // ...

    // get the symbol bitmaps
    syms = (JBIG2Bitmap **)gmallocn(numSyms, sizeof(JBIG2Bitmap *));
    if (numSyms > 0 && !syms) {
        return;
    }
    kk = 0;
    for (i = 0; i < nRefSegs; ++i) {
        if ((seg = findSegment(refSegs[i]))) {
            if (seg->getType() == jbig2SegSymbolDict) {
                symbolDict = (JBIG2SymbolDict *)seg;
                for (k = 0; k < symbolDict->getSize(); ++k) {
                    syms[kk++] = symbolDict->getBitmap(k);
                }
            }
        }
    }
    //...
}
```

We can inmediately see that, first an integer's value (numSyms) is calculated within a for and an if user-controlled statement:

```c
unsigned int numSyms, symCodeLen;
//...
numSyms = 0;
for (i = 0; i < nRefSegs; ++i) {
    if ((seg = findSegment(refSegs[i]))) {
        if (seg->getType() == jbig2SegSymbolDict) {
            numSyms += ((JBIG2SymbolDict *)seg)->getSize();
```

Since there is no validation, this calculation could lead to a integer overflow. Later, this value is used to allocated memory which in combination with the integer overflow risk can lead to an under-allocation:

```c
syms = (JBIG2Bitmap **)gmallocn(numSyms, sizeof(JBIG2Bitmap *));
```

Later, syms pointer gets used in a user-controlled for-loop in which receives data assignation, if an under-allocation gets performed, then this for loop can trigger an overcopying:

```c
for (i = 0; i < nRefSegs; ++i) {
    if ((seg = findSegment(refSegs[i]))) {
        if (seg->getType() == jbig2SegSymbolDict) {
            symbolDict = (JBIG2SymbolDict *)seg;
            for (k = 0; k < symbolDict->getSize(); ++k) {
                syms[kk++] = symbolDict->getBitmap(k);
```

<br>

#### 4.8. CVE-2021-22636. Texas Instruments + FreeRTOS (Open Source).

Consider the following code:


```c
int16_t _BundleCmdSignatureFile_Parse(
    OtaArchive_BundleCmdTable_t *pBundleCmdTable,
    uint8_t *pRecvBuf,    //XENO: ACID: TAR file received over network
    int16_t RecvBufLen,   //XENO: SACI: Size of TAR file received over network
    int16_t *ProcessedSize,
    uint32_t SigFileSize, //XENO: ACID: Size from TAR file headers
    uint8_t *pDigest)
{
    int16_t retVal = 0;
    char *  pSig = NULL;

    /* Get the entire signature file */
    retVal = GetEntireFile(pRecvBuf, RecvBufLen, ProcessedSize, SigFileSize,
                           &pSig);
    if(retVal < 0)
    {
        return(retVal);
    }
    if(retVal == GET_ENTIRE_FILE_CONTINUE)
    {
        return(ARCHIVE_STATUS_BUNDLE_CMD_SIGNATURE_CONTINUE);
    }

    /* Verify the signature using ECDSA */
    retVal = verifySignature(pSig, SigFileSize, pDigest);
    if(retVal < 0)
    {
        _SlOtaLibTrace((
                           "[_BundleCmdSignatureFile_Parse] "
                           "signature verification failed!\r\n"));
        return(retVal);
    }

    pBundleCmdTable->VerifiedSignature = 1;

    return(ARCHIVE_STATUS_BUNDLE_CMD_SIGNATURE_DOWNLOAD_DONE);
}
int16_t GetEntireFile(uint8_t *pRecvBuf,
                      int16_t RecvBufLen,
                      int16_t *ProcessedSize,
                      uint32_t FileSize,
                      char **pFile)
{
    int16_t copyLen = 0;
    static bool firstRun = TRUE;
    static int16_t TotalRecvBufLen = 0;

    if(firstRun)
    {
        TotalRecvBufLen = RecvBufLen;
        firstRun = FALSE;
        if(TotalRecvBufLen < FileSize)
        {
            /* Didn't receive the entire file in the first run. */
            /* Allocate a buffer in the size of the entire file and fill
                it in each round. */
            pTempBuf = (char*)malloc(FileSize + 1);
            if(pTempBuf == NULL)
            {
                /* Allocation failed, return error. */
                return(-1);
            }
            memcpy(pTempBuf, (char *)pRecvBuf, RecvBufLen);
            *ProcessedSize = RecvBufLen;

            /* didn't receive the entire file, try in the next packet */
            return(GET_ENTIRE_FILE_CONTINUE);
        }
        else
        {
            /* Received the entire file in the first run. */
            /* No additional memory allocation is needed. */
            *ProcessedSize = FileSize;
            *pFile = (char *)pRecvBuf;
        }
    }
    else
    {
        /* Avoid exceeding buffer size (FileSize + 1) */
        if(RecvBufLen > ((FileSize + 1) - TotalRecvBufLen))
        {
            copyLen = ((FileSize + 1) - TotalRecvBufLen);
        }
        else
        {
            copyLen = RecvBufLen;
        }

        /* Copy the received buffer from where we stopped the previous copy */
        memcpy(&(pTempBuf[TotalRecvBufLen]), (char *)pRecvBuf, copyLen);

        *ProcessedSize = copyLen;
        TotalRecvBufLen += copyLen;

        if(TotalRecvBufLen < FileSize)
        {
            /* didn't receive the entire file, try in the next packet */
            return(GET_ENTIRE_FILE_CONTINUE);
        }

        /* At this point we have the whole file */
        *pFile = (char *)pTempBuf;
    }

    /* Set static variables to initial values to allow retry in 
    case of a warning during the OTA process */
    firstRun = TRUE;
    TotalRecvBufLen = 0;

    return(GET_ENTIRE_FILE_DONE);
}
void ATTRIBUTE *malloc(size_t size)
{
    Header *packet;

    if (size == 0) {
        errno = EINVAL;
        return (NULL);
    }

    packet = (Header *)pvPortMalloc(size + sizeof(Header));

    if (packet == NULL) {
        errno = ENOMEM;
        return (NULL);
    }

    packet->header.actualBuf = (void *)packet;
    packet->header.size = size + sizeof(Header);

    return (packet + 1);
}
```

We can see that first, pRecvBuf, RecvBufLen and SigFileSize are user-controlled. This values are passed to *GetEntireFile()* and then they get included in the following code chunk:

```c
int16_t copyLen = 0;
static bool firstRun = TRUE;
static int16_t TotalRecvBufLen = 0;

if(firstRun)
{
    TotalRecvBufLen = RecvBufLen;
    firstRun = FALSE;
    if(TotalRecvBufLen < FileSize)
    {
        /* Didn't receive the entire file in the first run. */
        /* Allocate a buffer in the size of the entire file and fill
            it in each round. */
        pTempBuf = (char*)malloc(FileSize + 1);
        if(pTempBuf == NULL)
        {
            /* Allocation failed, return error. */
            return(-1);
        }
```

On it, we can see that firstRun at first gets assgined as TRUE, so the code flow jumps to the second if statement in which it compares TotalRecvBufLen < FileSize, since both values are user-controlled, this statement also is true and then comes malloc with maths over a user-controlled parameter.

Since *FileSize* is an unsigned integer, this addtion can go to an integer overflow passing from the most bigger value to a small one. Initially, if this was the normal malloc() function, FileSize biggest value should turn the operand 0 and malloc would return to us a NULL pointer, but the current malloc() function is wrapper around pvPortMalloc() function. If we check that implementation:

```c
void ATTRIBUTE *malloc(size_t size)
{
    Header *packet;

    if (size == 0) {
        errno = EINVAL;
        return (NULL);
    }

    packet = (Header *)pvPortMalloc(size + sizeof(Header));

    if (packet == NULL) {
        errno = ENOMEM;
        return (NULL);
    }
```

we can see that in fact is a wrapper around *pvPortMalloc()* and that if FileSize was a value satisfying:

```less
FileSize + 1 + sizeof(Header) = 1
```

Assuming that this addition is within the ring of module 32 integers, malloc function should return us a one byte-size pointer. This is, this malloc function is not protected against an underflow provoked by an integer overflow result by the way this function is called.

Automatically below, a memcpy() operation is performed with this underallocated pointer as a destination, using user-controlled values as source and length of the memcpy():

```c
memcpy(pTempBuf, (char *)pRecvBuf, RecvBufLen);
```

Leading to a what-where-write vulnerability.


<br>

