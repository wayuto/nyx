# Nyx v0.1

## Project Overview
Nyx is a programming language with syntax similar to Python, designed to generate high-performance C++ code. It is not a Python translator but an independent language that combines Python's simplicity with C++'s performance advantages.

## Language Features
- **Python-like Syntax**: Nyx's syntax is designed to resemble Python, reducing the learning curve.
- **Direct C++ Code Generation**: Nyx code is converted into efficient C++ code, which can be directly compiled into executable files.
- **Embedded C++ Support**: Seamlessly integrate existing C++ code using `importC` and `\cpp` syntax.
- **Type System**: Supports static type inference while retaining dynamic typing flexibility.
- **Cross-Platform**: The generated C++ code can run on any platform supporting C++.

## Syntax Examples
### Basic Syntax
```nyx
# Variable definition
a = 10
b = "Hello, Nyx!"

# Function definition
def add(x, y) {
    return x + y
}

# Control flow
if a > 5 {
    print(b)
} else {
    print("Too small")
}
```

### `importC` Syntax
Used to embed C/C++ header files:
```nyx
importC "path/to/header.h"
```
The generated C++ code will include the corresponding `#include "path/to/header.h"`.

### `\cpp` Syntax
Used to directly embed C++ code blocks:
```nyx
\cpp "std::cout << \"This is embedded C++ code\" << std::endl"
```

## Compilation Process
1. **Parse Nyx Code**: Convert Nyx code into an Abstract Syntax Tree (AST).
2. **Generate C++ Code**: Translate the AST into corresponding C++ code.
3. **Compile C++ Code** (Optional): Use `g++` to compile the generated C++ code into an executable.

## Common Use Cases
- **High-Performance Computing**: Leverage C++'s performance for compute-intensive tasks.
- **Embedded Development**: Directly manipulate hardware using `\cpp` syntax.
- **Code Migration**: Gradually migrate Python projects to C++ while retaining similar syntax.

## Usage Instructions
### Command
```bash
nyx --source input.nyx [--compile] [--output my_program] [--ast]
```

### Parameters
- `--source`: Specify the input Nyx file (required).
- `--compile`: Optional, compile the generated C++ code.
- `--output`: Specify the name of the output executable (default: `a.out`).
- `--ast`: Print the AST (for debugging).

## Dependencies
- `lark-parser` library (for parsing Nyx syntax).
- `g++` (optional, for compiling the generated C++ code).