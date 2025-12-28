---
layout: post
title: Race Conditions.
subtitle: Race Condition notes from OST2 course.
tags: [csoft]
---

### 1. Definition.

#### 1.1. Race Condition definition.

*Race Condition* is a term than refers to a set of bugs which arises when the behavior of a system depends on the relative timing or ordering of events, and that timing isn't properly controlled. The "race" is between two or more operations that need to happen in a specific order to produce correct results, but the system fails in guaranteeing that order.

A race condition emerges from a gap between checking a condition and acting on it. During that window—however brief—the state can change, invalidating the assumption your code just made.

Consider the following code:

```c
if (file_exists("/tmp/data")) {
    // Window of vulnerability here
    open_and_read("/tmp/data");
}
```

In the gap between checking and opening the file, some other process can interfere with it as a shared object.

We difference between two types of races condition in this course:

- **TOCTOU (Time-of-Check to Time-of-Use)** — the example above. You check something, then use it, assuming the check remains valid.
- **Double Fetch** — A double fetch occurs when kernel code reads the same user-space memory location twice, assuming the value remains constant between reads. Since user-space memory is under attacker control, a malicious thread can modify the value between the two fetches, breaking the kernel's assumptions.

 
The following diagram shows the TOCTOU race condition in-detail:

```
        PROCESS 1 (Victim)                    SHARED                   PROCESS 2 (Attacker)
              │                               RESOURCE (file)                 │
    Time      │                                  │                            │
      │       │                                  │                            │
      │       │  ┌─────────┐                     │                            │
      │       │  │ Verify()│                     │                            │
      │       │  │  Read ──────────────────────► │                            │
      │       │  └─────────┘                     │                            │
      │       │                                  │                            │
      │       │                                  |                            |
      │       │                                  │                            │
      │       │                                  │                            │
      │       │                                  |                            │
      │       │                                  |                            │
      │       │                                  |                            │
      │       │                                  │          Write             │
      │       │                                  │   ◄───────────────────     │
      │       │                                  │   (Attacker changes        │
      │       │                                  │    the resource)           │
      │       │                                  │                            │
      │       │              Write               │                            │ 
      │       │    ◄─────────────────────────    │  (Now operates on          │
      │       │                                  │   attacker-controlled      │
      │       │                                  │   resource!)               │
      │       │                                  │                            │
      │       │   TIME OF USE                    │                            │
      ▼       ▼                                  ▼                            ▼
```

If is well compassed, the writter can change the resource between the check and the use.

<br>

### 2. Exercises.

#### 2.1. CVE-2021-4207.

QEMU is an emulation and virtualization system. In the context of this bug, it's being used as a virtualization system, specifically via the use of the paravirtualized framebuffer video accelerator device, QXL. Paravirtualization is when you don't run an unmodified OS within the hypervisor, but instead run a modified one, that is aware of the hypervisor, and takes actions to make virtualization easier.

In the context of this attack, the guest VM is the attacker, and the QEMU hypervisor is the target. The attacker wants to break out of the virtualization, and gain code execution on the enclosing host, by exploiting a vulnerability in QEMU.

Consider the following C code:

```c
QEMUCursor *cursor_alloc(int width, int height) {
    QEMUCursor *c;
    int datasize = width * height * sizeof(uint32_t);

    c = g_malloc0(sizeof(QEMUCursor) + datasize);
    c->width  = width;
    c->height = height;
    c->refcount = 1;
    return c;
}


static void qxl_unpack_chunks(void *dest, size_t size, PCIQXLDevice *qxl, QXLDataChunk *chunk, uint32_t group_id) {
    uint32_t max_chunks = 32;
    size_t offset = 0;
    size_t bytes;

    for (;;) {
        bytes = MIN(size - offset, chunk->data_size);
        memcpy(dest + offset, chunk->data, bytes);
        offset += bytes;
        if (offset == size) {
            return;
        }
        chunk = qxl_phys2virt(qxl, chunk->next_chunk, group_id);
        if (!chunk) {
            return;
        }
        max_chunks--;
        if (max_chunks == 0) {
            return;
        }
    }
}

//XENO: cursor points to Guest OS shared memory, and is thus ACID
static QEMUCursor *qxl_cursor(PCIQXLDevice *qxl, QXLCursor *cursor, uint32_t group_id) {
    QEMUCursor *c;
    uint8_t *and_mask, *xor_mask;
    size_t size;

    c = cursor_alloc(cursor->header.width, cursor->header.height);
    c->hot_x = cursor->header.hot_spot_x;
    c->hot_y = cursor->header.hot_spot_y;
    switch (cursor->header.type) {
    case SPICE_CURSOR_TYPE_MONO:
        /* Assume that the full cursor is available in a single chunk. */
        size = 2 * cursor_get_mono_bpl(c) * c->height;
        if (size != cursor->data_size) {
            fprintf(stderr, "%s: bad monochrome cursor %ux%u with size %u\n",
                    __func__, c->width, c->height, cursor->data_size);
            goto fail;
        }
        and_mask = cursor->chunk.data;
        xor_mask = and_mask + cursor_get_mono_bpl(c) * c->height;
        cursor_set_mono(c, 0xffffff, 0x000000, xor_mask, 1, and_mask);
        if (qxl->debug > 2) {
            cursor_print_ascii_art(c, "qxl/mono");
        }
        break;
    case SPICE_CURSOR_TYPE_ALPHA:
        size = sizeof(uint32_t) * cursor->header.width * cursor->header.height;
        qxl_unpack_chunks(c->data, size, qxl, &cursor->chunk, group_id);
        if (qxl->debug > 2) {
            cursor_print_ascii_art(c, "qxl/alpha");
        }
        break;
    default:
        fprintf(stderr, "%s: not implemented: type %d\n",
                __func__, cursor->header.type);
        goto fail;
    }
    return c;

fail:
    cursor_put(c);
    return NULL;
}
```

Check that the cursor resource is fetched twice in the code.

- First, as parameters in the cursor_alloc() function, which returns a pointer to a cursor structu which some fields had been filled through the passed parameters:

    ```c
    QEMUCursor *cursor_alloc(int width, int height) {
        QEMUCursor *c;
        int datasize = width * height * sizeof(uint32_t);

        c = g_malloc0(sizeof(QEMUCursor) + datasize);
        c->width  = width;
        c->height = height;
        c->refcount = 1;
        return c;
    }

    static QEMUCursor *qxl_cursor(PCIQXLDevice *qxl, QXLCursor *cursor, uint32_t group_id) {
        QEMUCursor *c;
        uint8_t *and_mask, *xor_mask;
        size_t size;

        c = cursor_alloc(cursor->header.width, cursor->header.height);
        //...
    ```

    <br>

- Later, the code enters in a switch statement in which again access some cursor's specific fields to fill a variable (size), and then all along with the previously crafted 'c' structure, it call qxl_unpack_chunks() function:

    ```c
    //...
    size = sizeof(uint32_t) * cursor->header.width * cursor->header.height;
    qxl_unpack_chunks(c->data, size, qxl, &cursor->chunk, group_id);
    //...
    ```

This as a fact of matters constitutes a double fectch's race condition vulnerability.

The code is accesing twice an user-controlled resources (cursor height and weight) assuming that this resource value is constant between the calls and in is relating those two value in the execution flow:

```c
static void qxl_unpack_chunks(void *dest, size_t size, PCIQXLDevice *qxl, QXLDataChunk *chunk, uint32_t group_id) {
    uint32_t max_chunks = 32;
    size_t offset = 0;
    size_t bytes;

    for (;;) {
        bytes = MIN(size - offset, chunk->data_size);
        memcpy(dest + offset, chunk->data, bytes);
        offset += bytes;
        if (offset == size) {
            return;
        }
        chunk = qxl_phys2virt(qxl, chunk->next_chunk, group_id);
        if (!chunk) {
            return;
        }
        max_chunks--;
        if (max_chunks == 0) {
            return;
        }
    }
}
```

Inside the function above, a memcpy() operation, which is including *bytes* bytes of chunk->data (cursor user-controlled data field) on dest + offset. Thus, since bytes comes from our second fetch of the controlled parameters *heigh* and *weight* and *dest + offset* is the c structure, previously allocated with the first fetch, there can be a missleading between the allocation space and the number of bytes being copied leading to a heap-buffer overflow.

Note that this do not enters on the TOCTOU group of Race Conditions since no check is being made, just the same value fetched twice on the same procedure.

<br>

#### 2.2. CVE-2020-7460.

System calls are a mechanism for kernelspace to perform an action on userspace's behalf. FreeBSD implements the sendmsg() system call, to send messages from sockets:

```c
ssize_t sendmsg(int s, const struct msghdr *msg, int flags);
```

The *struct msghdr *msg parameter* has *void \*msg_control* and *socklen_t msg_controllen* fields, which represent an ancillary data buffer in userspace that the kernel should process in *freebsd32_copyin_control()*. The anticipated layout of this memory is shown below:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          msg_control buffer                                 │
├───────────┬───────────┬───────────┬───────────┬───────────┬─────────────────┤
│  cmsg_len │  cmsg_len │  cmsg_len │  cmsg_len │  cmsg_len │    cmsg_len     │
│  (header) │   bytes   │  (header) │   bytes   │  (header) │     bytes       │
│           │  (data)   │           │  (data)   │           │    (data)       │
└───────────┴─────┬─────┴───────────┴─────┬─────┴───────────┴────────┬────────┘
                  │                       │                          │
                  ▼                       ▼                          ▼
            data length            data length                 data length
          derived from           derived from                derived from
             cmsg_len               cmsg_len                    cmsg_len
```

Consider now the following C code:

```c
//XENO: buf is an ACID address/contents userspace buffer, buflen is also ACID
static int freebsd32_copyin_control(struct mbuf **mp, caddr_t buf, u_int buflen) {
	struct mbuf *m;
	void *md;
	u_int idx, len, msglen;
	int error;

	buflen = FREEBSD32_ALIGN(buflen);

	if (buflen > MCLBYTES)
		return (EINVAL);

	/*
	 * Iterate over the buffer and get the length of each message
	 * in there. This has 32-bit alignment and padding. Use it to
	 * determine the length of these messages when using 64-bit
	 * alignment and padding.
	 */
	idx = 0;
	len = 0;
	while (idx < buflen) {
		error = copyin(buf + idx, &msglen, sizeof(msglen));
		if (error)
			return (error);
		if (msglen < sizeof(struct cmsghdr))
			return (EINVAL);
		msglen = FREEBSD32_ALIGN(msglen);
		if (idx + msglen > buflen)
			return (EINVAL);
		idx += msglen;
		msglen += CMSG_ALIGN(sizeof(struct cmsghdr)) -
		    FREEBSD32_ALIGN(sizeof(struct cmsghdr));
		len += CMSG_ALIGN(msglen);
	}

	if (len > MCLBYTES)
		return (EINVAL);

	m = m_get(M_WAITOK, MT_CONTROL);
	if (len > MLEN)
		MCLGET(m, M_WAITOK);
	m->m_len = len;

	md = mtod(m, void *);
	while (buflen > 0) {
		error = copyin(buf, md, sizeof(struct cmsghdr));
		if (error)
			break;
		msglen = *(u_int *)md;
		msglen = FREEBSD32_ALIGN(msglen);

		/* Modify the message length to account for alignment. */
		*(u_int *)md = msglen + CMSG_ALIGN(sizeof(struct cmsghdr)) -
		    FREEBSD32_ALIGN(sizeof(struct cmsghdr));

		md = (char *)md + CMSG_ALIGN(sizeof(struct cmsghdr));
		buf += FREEBSD32_ALIGN(sizeof(struct cmsghdr));
		buflen -= FREEBSD32_ALIGN(sizeof(struct cmsghdr));

		msglen -= FREEBSD32_ALIGN(sizeof(struct cmsghdr));
		if (msglen > 0) {
			error = copyin(buf, md, msglen);
			if (error)
				break;
			md = (char *)md + CMSG_ALIGN(msglen);
			buf += msglen;
			buflen -= msglen;
		}
	}

	if (error)
		m_free(m);
	else
		*mp = m;
	return (error);
}
```

In the code there are two fetches of data from the buffer:

- First, from the while loop, the program takes data from the userspace shared memory buffer onto the *msglen* memory address. In this first while loop, this extracted data ends up in the *len* variable which later will be part of the *m*'s structure length field *m->m_len = len;*:

    ```c
    while (idx < buflen) {
		error = copyin(buf + idx, &msglen, sizeof(msglen));
		if (error)
			return (error);
		if (msglen < sizeof(struct cmsghdr))
			return (EINVAL);
		msglen = FREEBSD32_ALIGN(msglen);
		if (idx + msglen > buflen)
			return (EINVAL);
		idx += msglen;
		msglen += CMSG_ALIGN(sizeof(struct cmsghdr)) -
		    FREEBSD32_ALIGN(sizeof(struct cmsghdr));
		len += CMSG_ALIGN(msglen);
	}

	if (len > MCLBYTES)
		return (EINVAL);

	m = m_get(M_WAITOK, MT_CONTROL);
	if (len > MLEN)
		MCLGET(m, M_WAITOK);
	m->m_len = len;
    md = mtod(m, void *);
    ```

- Then, a second while loop enters in which a second fetch happens and the potential modified data from the shared buffer endsup in *msglen*:

    ```c
    while (buflen > 0) {
        error = copyin(buf, md, sizeof(struct cmsghdr));
        if (error)
            break;
        msglen = *(u_int *)md;
        //...
        msglen -= FREEBSD32_ALIGN(sizeof(struct cmsghdr));
		if (msglen > 0) {
			error = copyin(buf, md, msglen);
			if (error)
				break;
			md = (char *)md + CMSG_ALIGN(msglen);
			buf += msglen;
			buflen -= msglen;
		}
	}
    ```

Let's observe carefully that in the first fetch a memory space gets alloced in md, later the data gets again retrieved from the buffer and is used to write data on the previous allocated space, if the first fetch allocates a small memory region, the second fetch could lead to a overcopy leading to a heapbuffer overflow.

<br>

#### 2.3. CVE-2021-34514. "BlackSwan".

ALPC (Advanced Local Procedure Call) is a mechanism for communicating userspace to userspace, userspace to kernelspace, or kernelspace to kernelspace. Unlike the original LPC technology, ALPC is asynchronous, to improve performance through parallelism. Another performance improvement is using shared memory, to reduce data copy frequency.

Let's check the following code:

```c
// Heavily simplified pseudocode for the vulnerable function
void AlpcpCompleteDispatchMessage(_ALPC_DISPATCH_CONTEXT *DispatchContext)
{
	_ALPC_PORT *port;
	_KALPC_MESSAGE *message;
	_ALPC_COMPLETION_LIST *completionList;
	_ALPC_MESSAGE_ATTRIBUTES *attributes;
	_PORT_MESSAGE *userMappedMessage;

	void *userMappedMessageData;
	uint32_t completionBufferOffset;
	uint32_t bufferLength;
	uint32_t alignmentPadding = 0;

	port = DispatchContext->TargetPort;
	message = DispatchContext->Message;
	completionList = port->CompletionList;
	bufferLength = message->PortMessage.u1.s1.TotalLength;
	bufferLength += completionList->AttributeSize + alignmentPadding;

	// Finds free space in the completion list
	completionBufferOffset = AlpcpAllocateCompletionBuffer(port, bufferLength);

	userMappedMessage = (_PORT_MESSAGE *) ((uintptr_t) completionList->Data +
                                                       completionBufferOffset);

	// Message header is copied into shared user memory
	*userMappedMessage = message->PortMessage;
	userMappedMessageData = userMappedMessage + 0x1;

	// Copy message body into shared user memory
	if (message->DataUserVa == (void *)0x0){
		AlpcpReadMessageData(message, userMappedMessageData);
	}
	else
	{
		AlpcpGetDataFromUserVaSafe(message, userMappedMessageData);
	}

	if (completionList->AttributeFlags != 0x0) 
	{
		// Calulate offset and copy attributes into shared user memory
		attributes = (_ALPC_MESSAGE_ATTRIBUTES *) ( (uintptr t) userMappedMessage +	userMappedMessage->u1.s1.TotalLength + alignmentPadding);

		attributes->AllocatedAttributes = completionList->AttributeFlags;
		attributes->ValidAttributes = 0;
		AlpcpExposeAttributes(port, 0, message, completionList->AttributeFlags, attributes);
	}
	//...
}
```

Consider that the code is essentially using the information from the parameter to first allocate space for the message in what would be the first fetch:

```c
bufferLength = message->PortMessage.u1.s1.TotalLength; //1st fetch
bufferLength += completionList->AttributeSize + alignmentPadding;

// Finds free space in the completion list
completionBufferOffset = AlpcpAllocateCompletionBuffer(port, bufferLength);

userMappedMessage = (_PORT_MESSAGE *) ((uintptr_t) completionList->Data + completionBufferOffset);
```

Is worth to mention that what is passed as a parameter is a memory address to a shared memory region and what is being assignated in the stackframe of the function are fields from the structure pointed by te address passed as a parameter, this are, essentially more address in the form of "address + offset". This means that, despite this address being stored in the stackframe, this address referes to contents lying in a memory region the user controls and thus are suscetible to change between fetchs (race condition).

Then, the message is copied onto the alloced region in a second fetch:

```c	
// Message header is copied into shared user memory
*userMappedMessage = message->PortMessage;
userMappedMessageData = userMappedMessage + 0x1;

// Copy message body into shared user memory
if (message->DataUserVa == (void *)0x0){
    AlpcpReadMessageData(message, userMappedMessageData); //2nd fetch
}
else
{
    AlpcpGetDataFromUserVaSafe(message, userMappedMessageData);
}
```

As we say before, the contents of the buffer may be changed between fetches, leading first to an underallocation and later changing the contents to lead to an overcopy trigerring a heap-buffer overflow.

There is also another posibility since there is a third fetch:

```c
if (completionList->AttributeFlags != 0x0)	{
    // Calulate offset and copy attributes into shared user memory
    attributes = (_ALPC_MESSAGE_ATTRIBUTES *) ( (uintptr t) userMappedMessage + userMappedMessage->u1.s1.TotalLength + alignmentPadding);

    attributes->AllocatedAttributes = completionList->AttributeFlags;
    attributes->ValidAttributes = 0;
    AlpcpExposeAttributes(port, 0, message, completionList->AttributeFlags, attributes);
}
```

<br>