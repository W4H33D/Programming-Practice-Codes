# FileStats

## Overview

FileStats is a command-line utility written in C that provides detailed statistics about text files. It goes beyond simple character, whitespace, and line counts by also enumerating the occurrences of both lowercase and uppercase letters, presented in a clear, tabular format. This tool is designed to be a practical example of file handling, character processing, and basic data analysis in C.

---

## Lab Instructions (Original)

The original lab instructions that served as the foundation for this project can be found in `LAB.md` within this repository. This tool fulfills the core requirements of that lab while adding enhanced features.

---

## My Implementation - Beyond the Basic

While adhering to the core requirements of the lab, my solution extends the functionality to provide a more comprehensive analysis, making it a more versatile "tool."

### Key Enhancements:

* **Uppercase Letter Counts:** In addition to lowercase letters, the tool also counts and displays the occurrences of each uppercase letter.
* **Structured Output:** The letter counts are presented in a clear, aligned table, making the output easy to read and compare.
* **Command-Line Argument Handling:** The program expects a file path as a command-line argument, making it a flexible utility that can analyze any specified text file.
* **Usage Information:** If no file is provided or an invalid number of arguments is given, the tool provides clear usage instructions.

---

## Features

* Counts total characters in a file.
* Counts total whitespaces.
* Counts total lines.
* Counts occurrences of each lowercase letter (a-z).
* Counts occurrences of each uppercase letter (A-Z).
* Provides clear error messages and usage instructions.

---

## How to Build and Run

This project uses CMake for its build system, making it straightforward to compile across different platforms.

### Prerequisites

* A C compiler (e.g., GCC, Clang)
* CMake (version 3.10 or higher recommended)

### Building the Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/FileStats.git](https://github.com/YOUR_USERNAME/FileStats.git)
    cd FileStats
    ```
    (Replace `YOUR_USERNAME` with your actual GitHub username)

2.  **Create a build directory:**
    ```bash
    mkdir build
    cd build
    ```

3.  **Run CMake to configure the project:**
    ```bash
    cmake ..
    ```

4.  **Build the executable:**
    ```bash
    cmake --build .
    ```
    This will compile the `main.c` file and create an executable (e.g., `FileStats.exe` on Windows, `FileStats` on Linux/macOS) in the `build` directory (or a subdirectory like `build/Debug` or `build/Release` depending on your build system and IDE).

### Running the Tool

After building, you can run the `FileStats` executable from your terminal, providing the path to the text file you want to analyze.

#### Example Usage:

Assuming your executable is in `.\cmake-build-debug\FileStats.exe` (common for CLion/Windows builds) and you want to analyze `main.c`:

```bash
.\cmake-build-debug\FileStats.exe .\main.c
```

**Expected Output Format:**
If you run the tool without providing a file or with invalid parameters, you will see the usage instructions:
```
[-] Invalid Parameters
Usage:
--------
        D:\CLion Projects\FileStats\cmake-build-debug\FileStats.exe <text-file>

Example:
---------
        D:\CLion Projects\FileStats\cmake-build-debug\FileStats.exe example.txt
```

When successfully analyzing a file, the output will look similar to this (actual counts will vary based on the file content):

```
Total Charactors: 1498
Total White Spaces: 422
Total Lines: 59
| a | 46 | A |  3 |
| b |  1 | B |  0 |
| c | 34 | C |  2 |
| d | 11 | D |  0 |
| e | 57 | E |  3 |
| f | 22 | F |  2 |
| g | 10 | G |  0 |
| h | 25 | H |  0 |
| i | 45 | I |  2 |
| j |  0 | J |  0 |
| k |  1 | K |  0 |
| l | 45 | L |  4 |
| m |  7 | M |  0 |
| n | 47 | N |  1 |
| o | 37 | O |  1 |
| p | 36 | P |  1 |
| q |  0 | Q |  0 |
| r | 65 | R |  0 |
| s | 37 | S |  1 |
| t | 72 | T |  3 |
| u | 13 | U |  2 |
| v |  6 | V |  0 |
| w |  7 | W |  1 |
| x |  4 | X |  0 |
| y |  0 | Y |  0 |
| z |  2 | Z |  2 |
```
