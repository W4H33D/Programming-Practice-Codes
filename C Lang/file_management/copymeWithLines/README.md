# COPY Me With LINES

A C program that copies a source file to a destination file, adding line numbers to each line.

---

## Lab Instructions

This project was created as part of a lab assignment from the **OpenEDG C Essentials** course.  
The goal was to practice:

- Working with files in C  
- Reading from and writing to files  
- Using command-line arguments  
- Dynamic memory allocation for buffers

**Scenario:**  
Write a program that copies itself (or any given file) and adds line numbers to each line. The program should:

1. Open the source file in read mode.  
2. Open/create the destination file in write mode.  
3. Read the source file line by line using a buffer.  
4. Write each line to the destination file, prefixing it with its line number.  
5. Optionally accept a buffer size argument to control how many bytes are read per line.  
6. Handle errors gracefully if files cannot be opened or memory cannot be allocated.  
7. Close all opened files and free allocated memory before exiting.

---

## Usage

```
Usage: ./COPYmeWithLINES <source file> <destination file> [buffer size]
```

- `<source file>`: The file from which content will be copied.  
- `<destination file>`: The file into which the content will be copied.  
- `[buffer size]`: Optional. The number of bytes used to read each line. If not specified, the default buffer size is 256 bytes.

**Example:**

```
./COPYmeWithLINES main.c maincopy.c 512
```


This copies `main.c` into `maincopy.c` using a 512-byte buffer for reading each line.

---

## Features

- Supports customizable buffer size to handle lines of varying lengths.  
- Validates command-line arguments and handles errors such as file access or memory allocation failures.  
- Outputs helpful usage information if incorrect arguments are provided.  
- Written in standard C, compatible with common compilers like GCC and Clang.

---

## Compilation

Use GCC or your preferred C compiler:

```bash
gcc -o COPYmeWithLINES COPYmeWithLINES.c
```
