---
layout: post
title: "Other Integer Issues."
subtitle: "Notes from Other Integer Issues course from OST2."
date: 2025-12-05 09:00:00 +0000
categories: ['Past Blogs', 'Binary Exploitation']
tags: ['memory-corruption', 'exploits']
author: German Sanmi
---


### 1. Definition.

This section is an extension about Integers Overflow issues. We are going to cover three topics:

- Incorrect Signed Sanity Checks.
- Signed or unsigned integer truncation.
- Signed Integer extension issues.

<br>

### 2. Incorrect Signed Sanity Checks.

#### 2.1. Definition.

Incorrect Signed Sanity Checks refers to the idea of bad sanity checks implementation due to the unprevention of negative values being allowed and later cast into the execution flow as unsigned values effectively bypassing the sanitization measure.

To be a bit more precise the issue arises when a signed integer is checked against an upper bound (len < MAX_SIZE) but the check fails to account for negative values. When that signed integer is later used in a context that interprets it as unsigned (like memcpy(dst, src, len) where the len parameter is size_t), 

<br>

#### 2.2. Examples.

##### 2.2.1 Trivial Example.

Let's consider the following C code.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main(int argc, char *argv[]){
    char buf[100];
    int size = strtoul(argv[1], NULL, 16);
    if(size > 100){
        printf("Nice try *ATTACKER*! But I'm too clever for you!!!\n");
        return;
    }
    memcpy(buf, argv[2], size);
    printf("We got an input string: %s\n", buf);
}
```

First, we declare an array of maximum 100 bytes width and then we capture the cli first argument from the user interpreted as a hexadecimal value to *size* /(a signed integer).

Then, in order to prevent a Linear Stack Buffer Overflow a comparative check is performed over *size*:

```c
if(size > 100){
    printf("Nice try *ATTACKER*! But I'm too clever for you!!!\n");
    return;
}
```

If size was an unsigned integer, this check would work just fine since every value bigger than 100 would be succesfully blocked and then pass as the third argument (length) to memcpy() function.

However, there is a subtle problem. On the signature of a function, there are defined parameter to pass to that function as datatypes. This means that, whenever you pass a value to a function, this values gets cast to the funtion's demanded datatype, for example, if we look over the memcpy() function definition:

```c
void * memcpy(void * destination, const void * source, size_t num);
```

We can see that the third argument gets cast to a *size_t* datatype, which means that if a signed value lands as the length argument of memcpy() it will be interpreted as an unsigned integer.

This link with the fact that *size* is a signed integer, so, lets consider that the user pass a negative value, for example, "0xFFFFFFFFFFFFFF9B" (-101), then the comparation -101 > 100 is
false, so the flow of execution goes towards memcpy, but when passed to memcpy "0xFFFFFFFFFFFFFF9B" is interpreted as an unsigned integer: "4,294,967,195", provoking an overcopy in the memcpy() function. 

It is said that signed sanity checks 50% of the times works 100% of the time.

<br>

##### 2.2.2. Bad Sanity Check 1.

Another example of signed sanity checks can be the following:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct my_header{
        unsigned int magic;
        int size;
} my_header_t;

// Under-allocate, over-copy, bad sanity check
void main(int argc, char * argv[]){
        my_header_t header;
        unsigned int alloc_size;
        header.magic = 0x6f6e6558;
        header.size = strtoul(argv[1], NULL, 16);
        if(header.size > 0x1000){
                printf("Nice try *ATTACKER*! But I'm too clever for you!!!\n");
                return;
        }
        alloc_size = header.size + sizeof(my_header_t);
        printf("String self-reported size = 0x%08X\n", header.size);
        printf("Allocation size = 0x%08X\n", alloc_size);
        char * buf = malloc(alloc_size);
        if(buf == NULL) return;
        printf("buf points to %p\n", buf);
        memcpy(buf, &header, sizeof(my_header_t));
        buf += sizeof(my_header_t);
        printf("memcpy()ing 0x%08X bytes into buf of size 0x%08X\n", header.size, alloc_size);
        memcpy(buf, argv[2], header.size);
        printf("We copied input string: %s\n", buf);
}
```

Again, cli argument from user gets passed to header.size (signed integer) and is used to first, alloc memory through an unsigned integer to a destination buffer which later is gonna be used in a memcpy() operation with user-controlled length:

```c
//...
header.size = strtoul(argv[1], NULL, 16);
//...
char * buf = malloc(alloc_size);
memcpy(buf, &header, sizeof(my_header_t));
buf += sizeof(my_header_t);
printf("memcpy()ing 0x%08X bytes into buf of size 0x%08X\n", header.size, alloc_size);
memcpy(buf, argv[2], header.size);
//...
```

Here the thing is kind of more convulate than the previous example, but vulnerable in anyway. 

A protection mechanism as an *if statement* to prevent header.size be bigger than certain value is implemented:  

```c
if(header.size > 0x1000){
        printf("Nice try *ATTACKER*! But I'm too clever for you!!!\n");
        return;
}
```

the issue is that again, header.size is signed datatype and this comparison does not protect against big absolute negative numbers being pass in to the execution flow.

Thus, if header.size was a value that satisfies:

```c
header.size + sizeof(my_header_t) = 1
```

First, a one-byte allocation would be performed and *buf* pointer would point to that chunk, then , lets note that header.size has to be big absolute negative value by force since *sizeof(my_header_t) = 8* and would be pass as a size_t datatype (unsigned) to memcpy(), meaning that from a negative near-cero value, as an unsigned, it would become a big absolute value provoking an overflow. 

<br>

##### 2.2.3. Bad Sanity Check 2.

Let's consider the following C code:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct my_header{
        unsigned int magic;
        int size;
} my_header_t;

// Under-allocate, over-copy, bad sanity check
void main(int argc, char * argv[]){
        my_header_t header;
        unsigned int alloc_size;
        header.magic = 0x6f6e6558;
        header.size = strtoul(argv[1], NULL, 16);
        if(header.size + sizeof(my_header_t) >= 0x100000000){
                printf("Nice try *ATTACKER*! But I'm too clever for you!!!\n");
                return;
        }
        alloc_size = header.size + sizeof(my_header_t);
        printf("String self-reported size = 0x%08X\n", header.size);
        printf("Allocation size = 0x%08X\n", alloc_size);
        char * buf = malloc(alloc_size);
        if(buf == NULL) return;
        printf("buf points to %p\n", buf);
        memcpy(buf, &header, sizeof(my_header_t));
        buf += sizeof(my_header_t);
        printf("memcpy()ing 0x%08X bytes into buf of size 0x%08X\n", header.size, alloc_size);
        memcpy(buf, argv[2], header.size);
        printf("We copied input string: %s\n", buf);
}
```

This code is kind of similar to the one before, but instead of implement a one-value comparison, is establishing a comparison of an addition of two different-sign dataypes.

Here, enters what in C is known as implicit conversions, an arithemtic operation of two values of the same datatypes and different signs results in the signed value to get automatically converted to the unsigned type before the arithmetic opeation resolution.

This means that, header.size bits-pattern value is interpreted as unsigned, thus a near-to-cero negative value can be interpreted as big postiive number which in addition with sizeof(my_header_t) could trigger an integer overflow and become a small positive value bypassing the size constraint. 

Then, this addition is again performed and assignated to alloc_size (unsigned integer) resulting in an under-allocation:

```c
alloc_size = header.size + sizeof(my_header_t);
printf("String self-reported size = 0x%08X\n", header.size);
printf("Allocation size = 0x%08X\n", alloc_size);
char * buf = malloc(alloc_size);
```

And later, a memcpy operation over this small memory region is performed passing header.size as length again as size_t (unsigned), thus triggering an over-copy.

```c
memcpy(buf, argv[2], header.size);
```

<br>

### 3. Integer Truncation.

As we disscussed in [Integer Overflow](https://gsanmi1.github.io/2025-12-05-IntegerOverflow-Underflow/) paper, every C value has associated a datatype which has a size and sometimes a sign (if is an integer subtype). Essentially, a value is a bit pattern stored in memory that acquires full definition when gets interpreted by the CPU following the instructions generated by the compiler.

*Integer Truncation* is a phenomenon in which the bit-pattern of an integer gets chopped off when the value gets converted from a wider datatype to a narrower one transforming the data in a defined way. 

When this size-datatype downgrade gets defined, the compiler generates an instruction to copy part of the bit-string of the value to another location, then when executed, the instruction makes the CPU strip off the bitchain lefting the lowerbits and operating with them as a new different value in the next instructions.

For example, consider the following conversion:

​```c
uint32_t wide = 0x0001FFFF;  // 131071 in decimal
uint16_t narrow = wide;      // narrow = 0xFFFF (65535)
​```

The 32-bit value '0x0001FFFF' has the following bit pattern:

​```less
0000 0000 0000 0001 1111 1111 1111 1111
|______upper 16____||____lower 16_____|
      discarded           retained
​```

When the C code gets compiled, the compiler would generate an instruction like the following:

```assem
mov eax, dword ptr [rbp - 8h]           ; In which original value exists
mov word ptr [rbp - 10h], ax            ; Copying to a new location only the 16 retained bits
```

The original value was 131071, but after truncation it becomes 65535 — a completely different value, which can lead to serious vulnerabilities if the program logic assumes the full original value is preserved.

<br>

#### 3.1. Trivial Example.

Let's consider the following C code:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct my_header{
        unsigned int magic;
        unsigned int size;
} my_header_t;

// Under-allocate (via truncation), over-copy
void main(int argc, char * argv[]){
        my_header_t header;
        unsigned short alloc_size;
        header.magic = 0x6f6e6558;
        header.size = strtoul(argv[1], NULL, 16);
        alloc_size = header.size + sizeof(my_header_t);
        printf("String self-reported size = 0x%08X\n", header.size);
        printf("Allocation size = 0x%08X\n", alloc_size);
        char * buf = malloc(alloc_size);
        if(buf == NULL) return;
        printf("buf points to %p\n", buf);
        memcpy(buf, &header, sizeof(my_header_t));
        buf += sizeof(my_header_t);
        printf("memcpy()ing 0x%08X bytes into buf of size 0x%08X\n", header.size, alloc_size);
        memcpy(buf, argv[2], header.size);
        printf("We copied input string: %s\n", buf);
}
```

This code is similar to the used in other examples but with the subtle differences that in this case, alloc_size is a short, not a int.

Thus, for example, consider that the user pass as the first cli parameter to the program (argv\[1\]), which is an int and occupies 4 bytes, have the value 0xFFFF0000 (two hex-digits per byte, 4 pairs of digits), then, this value would end up in header.size and later would be used in an arithmetic operation:

```c
header.size = strtoul(argv[1], NULL, 16);
alloc_size = header.size + sizeof(my_header_t);
```

Note that, at a first glance, 0xFFFF0000 + 0x00000008 = 0xFFFF0008 and nothing wrong happens regards to the integer overflow subject we studied before. However this int-wide value is now assigned to an narrower datatype (unsigned short), when performing the assignation, the compiler truncates the value to a short, keeping the two rightmost bytes effectively wrapping it to 0x0008 which is then saved in *alloc_size*.

As a result, an under-allocation is performed and later, the complete int-wide value (header.size) is used to perfom an memcpy() operation, triggering an over-copy:

```c
char * buf = malloc(alloc_size);
//...
memcpy(buf, argv[2], header.size);
```

<br>

### 4. Signed-Arithmetics. 

#### 4.1. Pointer arithmetics with signed integers.
Consider the following code:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Pointer arithmetic + sign extension - pase.c
int main(){
        char buf[8];
        char * ptr1, * ptr2;
        short size1 = 0x8000;
        int size2 = 0x80000000;
        ptr1 = buf + size1;
        ptr2 = buf + size2;
        printf("buf =  %p\n", buf);
        printf("ptr1 = %p\n", ptr1);
        printf("ptr2 = %p\n", ptr2);
        return 0;
}
```

Pointer arithmetics are being performed with signed integers which result to be negative values, the MAX_SIZE for an integer hexadecimal value always is 0x7FF..., both values are one bit over the maximum positive value and thus are small negative numbers, thus the arithmetic operation with pointer is not an addition, but a substraction, the pointer now points above the buffer an, for example, use it in a data-copy operation would result in an out-of-bounds. 

As a result, any operation performed with a signed datatype can lead to a misscalculation resulting in a potential security issue and must be reviewed carefully.

<br>

#### 4.2. Signed Extension.

Another example on how signed-datatype poorly handled can generate issue is through the sign extension mechanismo. In which a signed datatypes gets converted to a bigger size datatype preserving the sign:

```c
signed char offset = -1;           // Malicious input: -1
size_t array_index = offset;       // Sign extended to large positive.
// On 64-bit: array_index = 0xFFFFFFFFFFFFFFFF (huge number!)
```

If later this sign extension is used as an unsigned integer troubles can arise:

```c
char buffer[100];    
buffer[array_index] = 'X';     // Out-of-bounds access!
```

<br>

### 5. Exercises.

#### 5.1. CVE-2019-15948. 

Consider the following code:

```c
////ACID: where ptr_ll_pkt points after assignment
// Pseudocode from Ghidra decompilation
void process_adv_ind_pdu(int ptr_some_struct)
{
  byte bVar1;
  byte ll_len;
  uint n;
  uint uVar2;
  byte *ptr_ll_pkt;
  undefined local_40;
  byte local_3f;
  undefined auStack62 [0x6];
  undefined local_38;
  undefined stack_buffer [0x1f];
  undefined local_18;

  ptr_ll_pkt = (byte *)(DAT_0005b528 + (uint)*(ushort *)(ptr_some_struct + 0x8));
  bVar1 = *ptr_ll_pkt;
  ll_len = ptr_ll_pkt[0x1];
  uVar2 = (uint)bVar1 & 0xf;
  local_3f = (byte)(((uint)bVar1 << 0x19) >> 0x1f);
  FUN_00067554(auStack62,ptr_ll_pkt + 0x2,0x6);
  n = ((uint)ll_len & 0x3f) - 0x6 & 0xff;
  local_38 = (undefined)n;
  memcpy(stack_buffer,ptr_ll_pkt + 0x8,n);
  local_18 = *(undefined *)(ptr_some_struct + 0xa);
  if ((bVar1 & 0xf) == 0x0) {
    local_40 = 0x0;
  }
  else {
    if (uVar2 == 0x1) {
      local_40 = 0x1;
      local_38 = 0x0;
    }
    else {
      if (uVar2 == 0x2) {
        local_40 = 0x3;
      }
      else {
        if (uVar2 != 0x6) {
          return;
        }
        local_40 = 0x2;
      }
    }
  }
  FUN_000398e2(0x1,&local_40);
  return;
}
```

Let's observe that at first, a memcpy() operation is taking place:

```c
memcpy(stack_buffer,ptr_ll_pkt + 0x8,n);
```

Where, 

- *stack_buffer* is stack-buffer of [\0x1f\] slots.
- *ptr_ll_pkt* is user-controlled source.
- *n* is a user-controlled parameter with a fixed size.

Let's make counts:

```c
n = ((uint)ll_len & 0x3f) - 0x6 & 0xff;
```

*ll_len* is user-conttrolled, since is casted as a unsigned integer, then "(uint)ll_len & 0x3f" is also casted as unsigned integer and also the substraction "((uint)ll_len & 0x3f) - 0x6" is unsigned. Then, is *ll_len* is a value that makes 0 the term "((uint)ll_len & 0x3f)", then, -0x6 is (as an unsigned integer), 0xFFFFFFFA which masked with 0xFF is 0xFA.

So *n* can have as maxim value 0xFA versus the size of the array which is 0x1F, thus a stack buffer overflow arises.

<br>

#### 5.2. CVE-2020-15999.

Google Chrome uses the open source FreeType project, which renders fonts and PNG images embedded in fonts.


Consider the following C code. The code attemps to process PNG images in fonts. Retrieves the images width and height from the header stores them in an special structure, calculates the bitmap size and allocates it back in store for that size.

Then calls for another library function to copy data from the PNG int the allocate space before.

```c
#if CHAR_BIT == 8 && UCHAR_MAX == 255
   typedef unsigned char png_byte;
#else
#  error "libpng requires 8-bit bytes"
#endif

typedef char  FT_String;
typedef unsigned char  FT_Byte;
typedef signed char  FT_Char;
typedef unsigned char  FT_Bool;
typedef signed short  FT_FWord;   /* distance in FUnits */
typedef unsigned short  FT_UFWord;  /* unsigned distance */
typedef signed short  FT_Short;
typedef unsigned short  FT_UShort;
typedef signed int  FT_Int;
typedef unsigned int  FT_UInt;
typedef signed long  FT_Long;
typedef unsigned long  FT_ULong;

typedef struct  FT_Bitmap_
{
  unsigned int    rows;
  unsigned int    width;
  int             pitch;
  unsigned char*  buffer;
  unsigned short  num_grays;
  unsigned char   pixel_mode;
  unsigned char   palette_mode;
  void*           palette;
} FT_Bitmap;

typedef struct  TT_SBit_MetricsRec_
{
  FT_UShort  height;
  FT_UShort  width;

  FT_Short   horiBearingX;
  FT_Short   horiBearingY;
  FT_UShort  horiAdvance;

  FT_Short   vertBearingX;
  FT_Short   vertBearingY;
  FT_UShort  vertAdvance;

} TT_SBit_MetricsRec, *TT_SBit_Metrics;

////ACID: data, png_len
  FT_LOCAL_DEF( FT_Error )
  Load_SBit_Png( FT_GlyphSlot     slot,
                 FT_Int           x_offset,
                 FT_Int           y_offset,
                 FT_Int           pix_bits,
                 TT_SBit_Metrics  metrics,
                 FT_Memory        memory,
                 FT_Byte*         data,
                 FT_UInt          png_len,
                 FT_Bool          populate_map_and_metrics, //KC: Assume true
                 FT_Bool          metrics_only )
  {
    FT_Bitmap    *map   = &slot->bitmap;
    FT_Error      error = FT_Err_Ok;
    FT_StreamRec  stream;

    png_structp  png;
    png_infop    info;
    png_uint_32  imgWidth, imgHeight;
    int         bitdepth, color_type, interlace;
    FT_Int      i;
    png_byte*  *rows = NULL; /* pacify compiler */

    // ...

    FT_Stream_OpenMemory( &stream, data, png_len ); //KC: data ACID-> stream

    png = png_create_read_struct( PNG_LIBPNG_VER_STRING,
                                  &error,
                                  error_callback,
                                  warning_callback );

    // ...

    png_set_read_fn( png, &stream, read_data_from_FT_Stream ); //KC: stream ACID-> png

    png_read_info( png, info );
    png_get_IHDR( png, info,
                  &imgWidth, &imgHeight,
                  &bitdepth, &color_type, &interlace,
                  NULL, NULL );

    if ( error                                    ||
         ( !populate_map_and_metrics              &&
           ( (FT_Int)imgWidth  != metrics->width  ||
             (FT_Int)imgHeight != metrics->height ) ) )
      goto DestroyExit;

    if ( populate_map_and_metrics )
    {
      metrics->width  = (FT_UShort)imgWidth;
      metrics->height = (FT_UShort)imgHeight;

      map->width      = metrics->width;
      map->rows       = metrics->height;
      map->pixel_mode = FT_PIXEL_MODE_BGRA;
      map->pitch      = (int)( map->width * 4 );
      map->num_grays  = 256;

      /* reject too large bitmaps similarly to the rasterizer */
      if ( map->rows > 0x7FFF || map->width > 0x7FFF )
      {
        error = FT_THROW( Array_Too_Large );
        goto DestroyExit;
      }
    }

    // ...

    if ( populate_map_and_metrics )
    {
      /* this doesn't overflow: 0x7FFF * 0x7FFF * 4 < 2^32 */
      FT_ULong  size = map->rows * (FT_ULong)map->pitch;


      error = ft_glyphslot_alloc_bitmap( slot, size );
      if ( error )
        goto DestroyExit;
    }

    if ( FT_NEW_ARRAY( rows, imgHeight ) ) //KC: realloc(rows, imgHeight*sizeof(ptr))
    {                                      //KC: and memset() to 0
      error = FT_THROW( Out_Of_Memory );
      goto DestroyExit;
    }

    for ( i = 0; i < (FT_Int)imgHeight; i++ )
      rows[i] = map->buffer + ( y_offset + i ) * map->pitch + x_offset * 4;

    png_read_image( png, rows ); //KC: Uses the same imgWidth/Height from png_get_IHDR() to read the PNG into rows[]
  }

/* Pointers to pointers; i.e. arrays */
typedef png_byte        * * png_bytepp;

struct png_struct_def
{
#ifdef PNG_SETJMP_SUPPORTED
   jmp_buf jmp_buf_local;     /* New name in 1.6.0 for jmp_buf in png_struct */
   png_longjmp_ptr longjmp_fn;/* setjmp non-local goto function. */
   jmp_buf *jmp_buf_ptr;      /* passed to longjmp_fn */
   size_t jmp_buf_size;       /* size of the above, if allocated */
#endif
   png_error_ptr error_fn;    /* function for printing errors and aborting */
#ifdef PNG_WARNINGS_SUPPORTED
   png_error_ptr warning_fn;  /* function for printing warnings */
#endif
   png_voidp error_ptr;       /* user supplied struct for error functions */
   png_rw_ptr write_data_fn;  /* function for writing output data */
   png_rw_ptr read_data_fn;   /* function for reading input data */
   png_voidp io_ptr;          /* ptr to application struct for I/O functions */

#ifdef PNG_READ_USER_TRANSFORM_SUPPORTED
   png_user_transform_ptr read_user_transform_fn; /* user read transform */
#endif

#ifdef PNG_WRITE_USER_TRANSFORM_SUPPORTED
   png_user_transform_ptr write_user_transform_fn; /* user write transform */
#endif

/* These were added in libpng-1.0.2 */
#ifdef PNG_USER_TRANSFORM_PTR_SUPPORTED
#if defined(PNG_READ_USER_TRANSFORM_SUPPORTED) || \
    defined(PNG_WRITE_USER_TRANSFORM_SUPPORTED)
   png_voidp user_transform_ptr; /* user supplied struct for user transform */
   png_byte user_transform_depth;    /* bit depth of user transformed pixels */
   png_byte user_transform_channels; /* channels in user transformed pixels */
#endif
#endif

   png_uint_32 mode;          /* tells us where we are in the PNG file */
   png_uint_32 flags;         /* flags indicating various things to libpng */
   png_uint_32 transformations; /* which transformations to perform */

   png_uint_32 zowner;        /* ID (chunk type) of zstream owner, 0 if none */
   z_stream    zstream;       /* decompression structure */

#ifdef PNG_WRITE_SUPPORTED
   png_compression_bufferp zbuffer_list; /* Created on demand during write */
   uInt                    zbuffer_size; /* size of the actual buffer */

   int zlib_level;            /* holds zlib compression level */
   int zlib_method;           /* holds zlib compression method */
   int zlib_window_bits;      /* holds zlib compression window bits */
   int zlib_mem_level;        /* holds zlib compression memory level */
   int zlib_strategy;         /* holds zlib compression strategy */
#endif
/* Added at libpng 1.5.4 */
#ifdef PNG_WRITE_CUSTOMIZE_ZTXT_COMPRESSION_SUPPORTED
   int zlib_text_level;            /* holds zlib compression level */
   int zlib_text_method;           /* holds zlib compression method */
   int zlib_text_window_bits;      /* holds zlib compression window bits */
   int zlib_text_mem_level;        /* holds zlib compression memory level */
   int zlib_text_strategy;         /* holds zlib compression strategy */
#endif
/* End of material added at libpng 1.5.4 */
/* Added at libpng 1.6.0 */
#ifdef PNG_WRITE_SUPPORTED
   int zlib_set_level;        /* Actual values set into the zstream on write */
   int zlib_set_method;
   int zlib_set_window_bits;
   int zlib_set_mem_level;
   int zlib_set_strategy;
#endif

   png_uint_32 width;         /* width of image in pixels */
   png_uint_32 height;        /* height of image in pixels */
   png_uint_32 num_rows;      /* number of rows in current pass */
   png_uint_32 usr_width;     /* width of row at start of write */
   size_t rowbytes;           /* size of row in bytes */
   png_uint_32 iwidth;        /* width of current interlaced row in pixels */
   png_uint_32 row_number;    /* current row in interlace pass */
   png_uint_32 chunk_name;    /* PNG_CHUNK() id of current chunk */
   png_bytep prev_row;        /* buffer to save previous (unfiltered) row.
                               * While reading this is a pointer into
                               * big_prev_row; while writing it is separately
                               * allocated if needed.
                               */
   png_bytep row_buf;         /* buffer to save current (unfiltered) row.
                               * While reading, this is a pointer into
                               * big_row_buf; while writing it is separately
                               * allocated.
                               */
#ifdef PNG_WRITE_FILTER_SUPPORTED
   png_bytep try_row;    /* buffer to save trial row when filtering */
   png_bytep tst_row;    /* buffer to save best trial row when filtering */
#endif
   size_t info_rowbytes;      /* Added in 1.5.4: cache of updated row bytes */

   png_uint_32 idat_size;     /* current IDAT size for read */
   png_uint_32 crc;           /* current chunk CRC value */
   png_colorp palette;        /* palette from the input file */
   png_uint_16 num_palette;   /* number of color entries in palette */

/* Added at libpng-1.5.10 */
#ifdef PNG_CHECK_FOR_INVALID_INDEX_SUPPORTED
   int num_palette_max;       /* maximum palette index found in IDAT */
#endif

   png_uint_16 num_trans;     /* number of transparency values */
   png_byte compression;      /* file compression type (always 0) */
   png_byte filter;           /* file filter type (always 0) */
   png_byte interlaced;       /* PNG_INTERLACE_NONE, PNG_INTERLACE_ADAM7 */
   png_byte pass;             /* current interlace pass (0 - 6) */
   png_byte do_filter;        /* row filter flags (see PNG_FILTER_ in png.h ) */
   png_byte color_type;       /* color type of file */
   png_byte bit_depth;        /* bit depth of file */
   png_byte usr_bit_depth;    /* bit depth of users row: write only */
   png_byte pixel_depth;      /* number of bits per pixel */
   png_byte channels;         /* number of channels in file */
#ifdef PNG_WRITE_SUPPORTED
   png_byte usr_channels;     /* channels at start of write: write only */
#endif
   png_byte sig_bytes;        /* magic bytes read/written from start of file */
   png_byte maximum_pixel_depth;
                              /* pixel depth used for the row buffers */
   png_byte transformed_pixel_depth;
                              /* pixel depth after read/write transforms */
#if ZLIB_VERNUM >= 0x1240
   png_byte zstream_start;    /* at start of an input zlib stream */
#endif /* Zlib >= 1.2.4 */
#if defined(PNG_READ_FILLER_SUPPORTED) || defined(PNG_WRITE_FILLER_SUPPORTED)
   png_uint_16 filler;           /* filler bytes for pixel expansion */
#endif

#if defined(PNG_bKGD_SUPPORTED) || defined(PNG_READ_BACKGROUND_SUPPORTED) ||\
   defined(PNG_READ_ALPHA_MODE_SUPPORTED)
   png_byte background_gamma_type;
   png_fixed_point background_gamma;
   png_color_16 background;   /* background color in screen gamma space */
#ifdef PNG_READ_GAMMA_SUPPORTED
   png_color_16 background_1; /* background normalized to gamma 1.0 */
#endif
#endif /* bKGD */

#ifdef PNG_WRITE_FLUSH_SUPPORTED
   png_flush_ptr output_flush_fn; /* Function for flushing output */
   png_uint_32 flush_dist;    /* how many rows apart to flush, 0 - no flush */
   png_uint_32 flush_rows;    /* number of rows written since last flush */
#endif

#ifdef PNG_READ_GAMMA_SUPPORTED
   int gamma_shift;      /* number of "insignificant" bits in 16-bit gamma */
   png_fixed_point screen_gamma; /* screen gamma value (display_exponent) */

   png_bytep gamma_table;     /* gamma table for 8-bit depth files */
   png_uint_16pp gamma_16_table; /* gamma table for 16-bit depth files */
#if defined(PNG_READ_BACKGROUND_SUPPORTED) || \
   defined(PNG_READ_ALPHA_MODE_SUPPORTED) || \
   defined(PNG_READ_RGB_TO_GRAY_SUPPORTED)
   png_bytep gamma_from_1;    /* converts from 1.0 to screen */
   png_bytep gamma_to_1;      /* converts from file to 1.0 */
   png_uint_16pp gamma_16_from_1; /* converts from 1.0 to screen */
   png_uint_16pp gamma_16_to_1; /* converts from file to 1.0 */
#endif /* READ_BACKGROUND || READ_ALPHA_MODE || RGB_TO_GRAY */
#endif

#if defined(PNG_READ_GAMMA_SUPPORTED) || defined(PNG_sBIT_SUPPORTED)
   png_color_8 sig_bit;       /* significant bits in each available channel */
#endif

#if defined(PNG_READ_SHIFT_SUPPORTED) || defined(PNG_WRITE_SHIFT_SUPPORTED)
   png_color_8 shift;         /* shift for significant bit transformation */
#endif

#if defined(PNG_tRNS_SUPPORTED) || defined(PNG_READ_BACKGROUND_SUPPORTED) \
 || defined(PNG_READ_EXPAND_SUPPORTED) || defined(PNG_READ_BACKGROUND_SUPPORTED)
   png_bytep trans_alpha;           /* alpha values for paletted files */
   png_color_16 trans_color;  /* transparent color for non-paletted files */
#endif

   png_read_status_ptr read_row_fn;   /* called after each row is decoded */
   png_write_status_ptr write_row_fn; /* called after each row is encoded */
#ifdef PNG_PROGRESSIVE_READ_SUPPORTED
   png_progressive_info_ptr info_fn; /* called after header data fully read */
   png_progressive_row_ptr row_fn;   /* called after a prog. row is decoded */
   png_progressive_end_ptr end_fn;   /* called after image is complete */
   png_bytep save_buffer_ptr;        /* current location in save_buffer */
   png_bytep save_buffer;            /* buffer for previously read data */
   png_bytep current_buffer_ptr;     /* current location in current_buffer */
   png_bytep current_buffer;         /* buffer for recently used data */
   png_uint_32 push_length;          /* size of current input chunk */
   png_uint_32 skip_length;          /* bytes to skip in input data */
   size_t save_buffer_size;          /* amount of data now in save_buffer */
   size_t save_buffer_max;           /* total size of save_buffer */
   size_t buffer_size;               /* total amount of available input data */
   size_t current_buffer_size;       /* amount of data now in current_buffer */
   int process_mode;                 /* what push library is currently doing */
   int cur_palette;                  /* current push library palette index */

#endif /* PROGRESSIVE_READ */

#if defined(__TURBOC__) && !defined(_Windows) && !defined(__FLAT__)
/* For the Borland special 64K segment handler */
   png_bytepp offset_table_ptr;
   png_bytep offset_table;
   png_uint_16 offset_table_number;
   png_uint_16 offset_table_count;
   png_uint_16 offset_table_count_free;
#endif

#ifdef PNG_READ_QUANTIZE_SUPPORTED
   png_bytep palette_lookup; /* lookup table for quantizing */
   png_bytep quantize_index; /* index translation for palette files */
#endif

/* Options */
#ifdef PNG_SET_OPTION_SUPPORTED
   png_uint_32 options;           /* On/off state (up to 16 options) */
#endif

#if PNG_LIBPNG_VER < 10700
/* To do: remove this from libpng-1.7 */
#ifdef PNG_TIME_RFC1123_SUPPORTED
   char time_buffer[29]; /* String to hold RFC 1123 time text */
#endif
#endif

/* New members added in libpng-1.0.6 */

   png_uint_32 free_me;    /* flags items libpng is responsible for freeing */

#ifdef PNG_USER_CHUNKS_SUPPORTED
   png_voidp user_chunk_ptr;
#ifdef PNG_READ_USER_CHUNKS_SUPPORTED
   png_user_chunk_ptr read_user_chunk_fn; /* user read chunk handler */
#endif
#endif

#ifdef PNG_SET_UNKNOWN_CHUNKS_SUPPORTED
   int          unknown_default; /* As PNG_HANDLE_* */
   unsigned int num_chunk_list;  /* Number of entries in the list */
   png_bytep    chunk_list;      /* List of png_byte[5]; the textual chunk name
                                  * followed by a PNG_HANDLE_* byte */
#endif

/* New members added in libpng-1.0.3 */
#ifdef PNG_READ_RGB_TO_GRAY_SUPPORTED
   png_byte rgb_to_gray_status;
   /* Added in libpng 1.5.5 to record setting of coefficients: */
   png_byte rgb_to_gray_coefficients_set;
   /* These were changed from png_byte in libpng-1.0.6 */
   png_uint_16 rgb_to_gray_red_coeff;
   png_uint_16 rgb_to_gray_green_coeff;
   /* deleted in 1.5.5: rgb_to_gray_blue_coeff; */
#endif

/* New member added in libpng-1.6.36 */
#if defined(PNG_READ_EXPAND_SUPPORTED) && \
    defined(PNG_ARM_NEON_IMPLEMENTATION)
   png_bytep riffled_palette; /* buffer for accelerated palette expansion */
#endif

/* New member added in libpng-1.0.4 (renamed in 1.0.9) */
#if defined(PNG_MNG_FEATURES_SUPPORTED)
/* Changed from png_byte to png_uint_32 at version 1.2.0 */
   png_uint_32 mng_features_permitted;
#endif

/* New member added in libpng-1.0.9, ifdef'ed out in 1.0.12, enabled in 1.2.0 */
#ifdef PNG_MNG_FEATURES_SUPPORTED
   png_byte filter_type;
#endif

/* New members added in libpng-1.2.0 */

/* New members added in libpng-1.0.2 but first enabled by default in 1.2.0 */
#ifdef PNG_USER_MEM_SUPPORTED
   png_voidp mem_ptr;             /* user supplied struct for mem functions */
   png_malloc_ptr malloc_fn;      /* function for allocating memory */
   png_free_ptr free_fn;          /* function for freeing memory */
#endif

/* New member added in libpng-1.0.13 and 1.2.0 */
   png_bytep big_row_buf;         /* buffer to save current (unfiltered) row */

#ifdef PNG_READ_QUANTIZE_SUPPORTED
/* The following three members were added at version 1.0.14 and 1.2.4 */
   png_bytep quantize_sort;          /* working sort array */
   png_bytep index_to_palette;       /* where the original index currently is
                                        in the palette */
   png_bytep palette_to_index;       /* which original index points to this
                                         palette color */
#endif

/* New members added in libpng-1.0.16 and 1.2.6 */
   png_byte compression_type;

#ifdef PNG_USER_LIMITS_SUPPORTED
   png_uint_32 user_width_max;
   png_uint_32 user_height_max;

   /* Added in libpng-1.4.0: Total number of sPLT, text, and unknown
    * chunks that can be stored (0 means unlimited).
    */
   png_uint_32 user_chunk_cache_max;

   /* Total memory that a zTXt, sPLT, iTXt, iCCP, or unknown chunk
    * can occupy when decompressed.  0 means unlimited.
    */
   png_alloc_size_t user_chunk_malloc_max;
#endif

/* New member added in libpng-1.0.25 and 1.2.17 */
#ifdef PNG_READ_UNKNOWN_CHUNKS_SUPPORTED
   /* Temporary storage for unknown chunk that the library doesn't recognize,
    * used while reading the chunk.
    */
   png_unknown_chunk unknown_chunk;
#endif

/* New member added in libpng-1.2.26 */
   size_t old_big_row_buf_size;

#ifdef PNG_READ_SUPPORTED
/* New member added in libpng-1.2.30 */
  png_bytep        read_buffer;      /* buffer for reading chunk data */
  png_alloc_size_t read_buffer_size; /* current size of the buffer */
#endif
#ifdef PNG_SEQUENTIAL_READ_SUPPORTED
  uInt             IDAT_read_size;   /* limit on read buffer size for IDAT */
#endif

#ifdef PNG_IO_STATE_SUPPORTED
/* New member added in libpng-1.4.0 */
   png_uint_32 io_state;
#endif

/* New member added in libpng-1.5.6 */
   png_bytep big_prev_row;

/* New member added in libpng-1.5.7 */
   void (*read_filter[PNG_FILTER_VALUE_LAST-1])(png_row_infop row_info,
      png_bytep row, png_const_bytep prev_row);

#ifdef PNG_READ_SUPPORTED
#if defined(PNG_COLORSPACE_SUPPORTED) || defined(PNG_GAMMA_SUPPORTED)
   png_colorspace   colorspace;
#endif
#endif
};

/* Basic control structions.  Read libpng-manual.txt or libpng.3 for more info.
 *
 * png_struct is the cache of information used while reading or writing a single
 * PNG file.  One of these is always required, although the simplified API
 * (below) hides the creation and destruction of it.
 */
typedef struct png_struct_def png_struct;

#    ifndef PNG_RESTRICT
#      define PNG_RESTRICT __restrict
#    endif

/* Types with names ending 'p' are pointer types.  The corresponding types with
 * names ending 'rp' are identical pointer types except that the pointer is
 * marked 'restrict', which means that it is the only pointer to the object
 * passed to the function.  Applications should not use the 'restrict' types;
 * it is always valid to pass 'p' to a pointer with a function argument of the
 * corresponding 'rp' type.  Different compilers have different rules with
 * regard to type matching in the presence of 'restrict'.  For backward
 * compatibility libpng callbacks never have 'restrict' in their parameters and,
 * consequentially, writing portable application code is extremely difficult if
 * an attempt is made to use 'restrict'.
 */
typedef png_struct * PNG_RESTRICT png_structrp;


/* Read the entire image.  If the image has an alpha channel or a tRNS
 * chunk, and you have called png_handle_alpha()[*], you will need to
 * initialize the image to the current image that PNG will be overlaying.
 * We set the num_rows again here, in case it was incorrectly set in
 * png_read_start_row() by a call to png_read_update_info() or
 * png_start_read_image() if png_set_interlace_handling() wasn't called
 * prior to either of these functions like it should have been.  You can
 * only call this function once.  If you desire to have an image for
 * each pass of a interlaced image, use png_read_rows() instead.
 *
 * [*] png_handle_alpha() does not exist yet, as of this version of libpng
 */
void PNGAPI
png_read_image(png_structrp png_ptr, png_bytepp image)
{
   png_uint_32 i, image_height;
   int pass, j;
   png_bytepp rp;

   png_debug(1, "in png_read_image");

   if (png_ptr == NULL)
      return;

#ifdef PNG_READ_INTERLACING_SUPPORTED
   if ((png_ptr->flags & PNG_FLAG_ROW_INIT) == 0)
   {
      pass = png_set_interlace_handling(png_ptr);
      /* And make sure transforms are initialized. */
      png_start_read_image(png_ptr);
   }
   else
   {
      if (png_ptr->interlaced != 0 &&
          (png_ptr->transformations & PNG_INTERLACE) == 0)
      {
         /* Caller called png_start_read_image or png_read_update_info without
          * first turning on the PNG_INTERLACE transform.  We can fix this here,
          * but the caller should do it!
          */
         png_warning(png_ptr, "Interlace handling should be turned on when "
             "using png_read_image");
         /* Make sure this is set correctly */
         png_ptr->num_rows = png_ptr->height;
      }

      /* Obtain the pass number, which also turns on the PNG_INTERLACE flag in
       * the above error case.
       */
      pass = png_set_interlace_handling(png_ptr);
   }
#else
   if (png_ptr->interlaced)
      png_error(png_ptr,
          "Cannot read interlaced image -- interlace handler disabled");

   pass = 1;
#endif

   image_height=png_ptr->height;

   for (j = 0; j < pass; j++)
   {
      rp = image;
      for (i = 0; i < image_height; i++)
      {
         png_read_row(png_ptr, *rp, NULL);
         rp++;
      }
   }
}
```

The key of this vulnerability, according to what we explain above resides on the following block:

```c
//...
if ( error                                    ||
        ( !populate_map_and_metrics              &&
        ( (FT_Int)imgWidth  != metrics->width  ||
        (FT_Int)imgHeight != metrics->height ) ) )
goto DestroyExit;

if ( populate_map_and_metrics )
{
metrics->width  = (FT_UShort)imgWidth;
metrics->height = (FT_UShort)imgHeight;
//...
}
```

The width and the height of the PNG which is used to allocate space gets truncated since gets both converted from *int* to *short* without correct validation. As we seen before, this could lead to an under-allocation and later to an over-copy.

<br>

#### 5.3. CVE-2020-17087.

Consider the following C code:

```c
////ACID:SourceBuffer, SourceLength
NTSTATUS CfgAdtpFormatPropertyBlock(PBYTE SourceBuffer, USHORT SourceLength, PUNICODE_STRING Destination)
{
	CONST USHORT DestinationSize = (USHORT)(6 * SourceLength);
	PWCHAR OutputBuffer = BCryptAlloc(DestinationSize);

	for (USHORT i = 0; i < SourceLength; i++) {
		*OutputBuffer++ = "0123456789abcdef"[*SourceBuffer >> 4];
		*OutputBuffer++ = "0123456789abcdef"[*SourceBuffer & 0xF];
		*OutputBuffer++ = ' ';
		SourceBuffer++;
	}

 	Destination->MaximumLength = DestinationSize;
 	Destination->Length = DestinationSize - 2;
 	Destination->Buffer = OutputBuffer;

	return STATUS_SUCCESS;
}
```

This chunk of code is vulnerable to an overcopy due to underallocation result of integer overflow, OutputBuffer gets assignation in a for-loop when the break condition is i< Source Length. But the allocated space for this Buffer is DestinationSize which is 6 times SourceLength, this could provoke (assuming BCryptAlloc does not prevent it) that if SourceLength is (MAX_SHORT_SIZE + 1) / 6, then an underallocation is performed and out-of-bounds write is done.

<br>

#### 5.4. CVE-2021-33909. Sequoia.

Consider the following C code:

```c
////NOTE: Start reading the code at seq_read_iter()

/**
 * seq_has_overflowed - check if the buffer has overflowed
 * @m: the seq_file handle
 *
 * seq_files have a buffer which may overflow. When this happens a larger
 * buffer is reallocated and all the data will be printed again.
 * The overflow state is true when m->count == m->size.
 *
 * Returns true if the buffer received more than it can hold.
 */
static inline bool seq_has_overflowed(struct seq_file *m)
{
	return m->count == m->size;
}

//------------------------------------------------------------------------
135 static int show_mountinfo(struct seq_file *m, struct vfsmount *mnt) //KC: called by "m->op->show(m, p)" 
136 {
...
150                 seq_dentry(m, mnt->mnt_root, " \t\n\\");
//------------------------------------------------------------------------
523 int seq_dentry(struct seq_file *m, struct dentry *dentry, const char *esc)
524 {
525         char *buf;
526         size_t size = seq_get_buf(m, &buf);
...
529         if (size) {
530                 char *p = dentry_path(dentry, buf, size);
//------------------------------------------------------------------------
380 char *dentry_path(struct dentry *dentry, char *buf, int buflen)
381 {
382         char *p = NULL;
...
385         if (d_unlinked(dentry)) { //KC: assume true
386                 p = buf + buflen;
387                 if (prepend(&p, &buflen, "//deleted", 10) != 0)
//------------------------------------------------------------------------
 11 static int prepend(char **buffer, int *buflen, const char *str, int namelen)
 12 {
 13         *buflen -= namelen;
 14         if (*buflen < 0)
 15                 return -ENAMETOOLONG;
 16         *buffer -= namelen;
 17         memcpy(*buffer, str, namelen);
//------------------------------------------------------------------------

////ACID: Assume the attacker can control the underlying seq_file to cause the while(1) loop to occur as many times as they want
168 ssize_t seq_read_iter(struct kiocb *iocb, struct iov_iter *iter)
169 {
170         struct seq_file *m = iocb->ki_filp->private_data;
...
205         /* grab buffer if we didn't have one */
206         if (!m->buf) { //KC: assume this is NULL on the first iteration
207                 m->buf = seq_buf_alloc(m->size = PAGE_SIZE); //KC: m->size is a size_t
...
210         }
...
220         // get a non-empty record in the buffer
...
223         while (1) {
...
227                 err = m->op->show(m, p); //KC: This calls to show_mountinfo()
...
236                 if (!seq_has_overflowed(m)) // got it
237                         goto Fill;
238                 // need a bigger buffer
...
240                 kvfree(m->buf);
...
242                 m->buf = seq_buf_alloc(m->size <<= 1);
...
246         }
```