# The LLVM Compiler Infrastructure

This directory and its sub-directories contain source code for LLVM,
a toolkit for the construction of highly optimized compilers,
optimizers, and run-time environments.

The README briefly describes how to get started with building LLVM.
For more information on how to contribute to the LLVM project, please
take a look at the
[Contributing to LLVM](https://llvm.org/docs/Contributing.html) guide.

## Getting Started with the LLVM System

Taken from https://llvm.org/docs/GettingStarted.html.

### Overview

Welcome to the LLVM project!

The LLVM project has multiple components. The core of the project is
itself called "LLVM". This contains all of the tools, libraries, and header
files needed to process intermediate representations and converts it into
object files.  Tools include an assembler, disassembler, bitcode analyzer, and
bitcode optimizer.  It also contains basic regression tests.

C-like languages use the [Clang](http://clang.llvm.org/) front end.  This
component compiles C, C++, Objective-C, and Objective-C++ code into LLVM bitcode
-- and from there into object files, using LLVM.

Other components include:
the [libc++ C++ standard library](https://libcxx.llvm.org),
the [LLD linker](https://lld.llvm.org), and more.

### Getting the Source Code and Building LLVM

The LLVM Getting Started documentation may be out of date.  The [Clang
Getting Started](http://clang.llvm.org/get_started.html) page might have more
accurate information.


Here are the steps I followed that should work for a Linux system:

1. Checkout LLVM, and checkout branch modify-pass:

     * ``git clone https://github.com/log-of-e/llvm-project.git``
     * ``git checkout modify-pass``
    

     * Or, on windows, ``git clone --config core.autocrlf=false
    https://github.com/llvm/llvm-project.git``

2. Ensure python 3 is available globally to cmake:
    - pyenv instructions: https://github.com/pyenv/pyenv#installation, https://bgasparotto.com/install-pyenv-ubuntu-debian

  ```
  pyenv install 3.8.5
  pyenv global 3.8.5
  ```

3. Configure and build LLVM using cmake :

     * ``cd llvm-project``

     * ``mkdir build``

     * ``cd build``

     * `` cmake -G "Unix Makefiles"  -DCMAKE_BUILD_TYPE=Release   ../llvm``

        * ``Unix Makefiles`` --- for generating make-compatible parallel makefiles.

        Option explanations:


        * ``-DCMAKE_BUILD_TYPE=type`` --- Valid options for *type* are Debug,
          Release, RelWithDebInfo, and MinSizeRel. Default is Debug.

        


      * ``make -j8`` to run the build from directory `build`

        * Running a serial build will be **slow**.  To improve speed, try running a
          parallel build.  That's done by default in Ninja; for ``make``, use the option
          ``-j NNN``, where ``NNN`` is the number of parallel jobs, e.g. the number of
          CPUs you have.

      * For more information see [CMake](https://llvm.org/docs/CMake.html)

- I also consulted :
  - [Getting Started with LLVM](https://llvm.org/docs/GettingStarted.html#getting-started-with-llvm)
page for detailed information on configuring and compiling LLVM. 

  - [Directory Layout](https://llvm.org/docs/GettingStarted.html#directory-layout)
to learn about the layout of the source code tree.

4. I followed instructions to build `opt` (from  http://llvm.org/docs/WritingAnLLVMNewPMPass.html#running-a-pass-with-opt) From inside `build` directory:
  - ```
      make opt -j8
    ```
5. To test against the IR test case run the command from inside `build` directory: 
    ```
      ./bin/opt -disable-output  ../llvm/testcases/testir.ll    -passes=helloworld 

    ```
6. To test against the c program I followed the instructions to generate IR from : http://llvm.org/docs/GettingStarted.html#example-with-clang and then I ran:
    ```
    ./bin/opt -disable-output  ../llvm/testcases/test1.bc    -passes=helloworld
    ```

