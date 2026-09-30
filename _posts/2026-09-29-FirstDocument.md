---
layout: post
title: "Compiling first document: HelloWorld"
subtitle: "First steps into ARM64 dissasmebly code."
date: 2026-09-29 09:00:00 +0000
categories: ['ARM64','reverse-engineering']
tags: ['arm64']
author: German Sanmi
subject: arm64
lang: en
---

# 1. First Version.

We start out with a C++ program kind-of-like "Hello World" and break it down into several versions which are closer and closer to a high level assembly language (otherwise known as C). At the last step, we convert the C into ARM V8 assembly language.

<br>

## 1.1. Code.

Let be the following ```hello_world.c```:

```C++
#include <iostream>                                         // 1 
                                                            // 2 
using namespace std;                                        // 3 
                                                            // 4 
int main(int argc, char * argv[]) {                         // 5 
    while (*argv) {                                         // 6 
        cout << *(argv++) << endl;                          // 7 
    }                                                       // 8 
    return 0;                                               // 9 
}                                                           // 10
```

This code line by line does:

- Line 1; uses the preprocesor directive ```#``` to run ```include``` directive to add the standard input and output library code (iostream) allowing the program to use ```cout``` (```c```onsole ```out```put) to write to the console or ```cin``` to read from the keyboard instead of typing ```std::cout```.

- Line 3 uses ```namespace``` to allow the program to search identifiers inside the standards libraries ```std```, in our case ```iostream```. It tries to search in the code and if it is not able to find the identifier then namespace encourage the compiler to search in the imported stadanrd library.

- Line 5 introduces ```main``` function along with the number of arguments with which the program has been call with (```argc```) and the array of strings that conforms the arguments (```argv```)

- Lines 6,7 and 8 conformes a ```while``` loop.

    - First, we stablish the loop-type and the condition; the loop iterates until ```argv``` points to a nullpointer (```argv[argc]```)

    - In the meanwhile, it performs ```cout << *(argv++) << endl;``` which takes the current value of ```argv``` (and increment it ```type(char*)``` bytes), dereference it and pass it to ```cout``` and over this it adds a salt line. 

- Line 9 is the last line and returing 0 indicates the finalization of the code succesfully.

<br>

## 1.2. Compilation in ARM64.

Compile raw C++ code is process of four translations at once:

- **Preprocess Stage:** which is a lexic transformation that expands the code by executing preprocessing directives (```#```) among other things. This stage involves actions like: incorporating included libraries, expanding macros or evaluating conditionals or even deleting comentaries.    

- **Compilation Stage:** In this stage is where the transformation and optimization of the code in to assembly happens.

- **Assembly Stage:** The assembly language pass to machine code producing a binary object.

- **Linking Stage:** The binary object gets linked combining the libraries objects and the load code, resolving symbols into address inside the file.

We compile it in AArch64:

```bash
sudo apt install g++-aarch64-linux-gnu qemu-user
```

Then we compile:

```bash
$ aarch64-linux-gnu-g++ -std=c++17 -Wall -Wextra -o Hello_world helloworld.cpp 
helloworld.cpp: In function ‘int main(int, char**)’:
helloworld.cpp:5:14: warning: unused parameter ‘argc’ [-Wunused-parameter]
    5 | int main(int argc, char * argv[]) {
      |          ~~~~^~~~
```

And execute with QEMU, obtaining:

```bash
$ qemu-aarch64 -L /usr/aarch64-linux-gnu ./Hello_world hola mundo
./Hello_world
hola
mundo
```

<br>

## 1.3. Opening the file with Ghidra.

### 1.3.1. Opening the file.

Once we've installed our Ghidra we just import the file to our Ghidra's repository and let Ghidra to analize it, then in *Symbol Tree* we go to *Functions > main*. That would send us direct to the start of the main function of the program:

<div style="text-align:center">
<img src="{{ '/assets/images/past-blogs/GhidraARM/Ghidra1.png' | relative_url }}" text-align="center"/>
</div>


We can see that Ghidra provides in the right a rebuilt C code and on the left a decomposition of the Elf file. In the center lies the assembly code associated to the code.

<br>

### 1.3.2. Debugging the file.

Ghidra by default doesn't has a debugger, it is a interface which uses some other native debugger (depending on the running OS) through a Python's plugin and then provide the output to the user by transporting the output to his Dynamic Listing.

In Unix distributions we can install the ```protobuf``` plugin by:

```bash
cd <GhidraInstallDir>/Ghidra/Debug

python3 -m pip install --break-system-packages --no-index -f Debugger-rmi-trace/pypkg/dist -f Debugger-agent-gdb/pypkg/dist psutil protobuf
```

Is necesary to have ```python3```, ```pip```, ```gdb```, ```gdb-multiarch``` installed in the system (available via APT).

And set the root directory (sysroot) for our gdb, in order to make it able to load his enviroment:

```bash
echo 'set sysroot /usr/aarch64-linux-gnu' > /path/to/aarch64.gdb
```

Then, we open the debugger and open the file just as we did with the code browser. Since the file is already imported from the step $1.3.1$, then we only need to open the Elf again. Then we open it with the Debugger with "gdb+qemu" (gdb debugs by stoping the kernel and reading the snapshot information of the CPU, if the CPU is x86 we need a translator to ARM64, this is QEMU):

<div style="text-align:center">
<img src="{{ '/assets/images/past-blogs/GhidraARM/debugger.png' | relative_url }}" text-align="center"/>
</div>


Then, the configuration window will pop-up and we have to fill it up, it may happens that Ghidra would not recognize the options, we would have to introduce by hand:

| option | value |
|-|-|
| Image | ```/path/to/hello_world``` |
| Arguments | ```hello world``` |
| QEMU command | ```qemu-aarch64``` |
| Extra qemu arguments | ```-L /usr/aarch64-linux-gnu``` |
| gdb command | ```gdb-multiarch``` |
| gbd cmd args | ```--command=/path/to/aarch64.gdb``` |
| Architecture | ```auto``` |
| Endian | ```auto``` |
| QEMU TTY | - |
| Pull all section mappings | ```x``` |

