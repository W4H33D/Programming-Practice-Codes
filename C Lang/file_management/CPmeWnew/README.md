# File Copy Tool

A command-line utility written in C for copying the contents of one file to a new destination file. If the destination file already exists, the tool automatically appends an incremental number to the filename and retries up to five times.

This program was built as a solution to a file-handling lab exercise. For full problem details and constraints, see [LAB.md](LAB.md).

---

## ✨ Features

- Reads the contents of a source file provided by the user
- Attempts to copy the content into a new file
- If the destination file already exists, generates a new name like:
```
maincopy_1.c
maincopy_2.c
...
maincopy_5.c
```

- Stops after 5 attempts if all target filenames already exist
- Ensures all file operations are handled in **binary mode** for accurate byte copying
- Displays clear messages for both success and failure scenarios

---

## 📦 How to Build

You can compile the program using any standard C compiler or with CMake.

### Using GCC:
```bash
gcc main.c -o file_copy_tool
```

### Usage
```
./CPmeWnew <source_filename>
```

### Example
```
./CPmeWnew.exe main.c
```
If the copy is successful, the program prints:
```
Copy of the source file created: maincopy_1.c
```
If the source file cannot be opened:
```
Error opening file.
```
If all destination filenames are taken:
```
File count limit reached.
```
### Lab Description
This program was developed in response to a file-copying lab exercise involving:

- File reading and writing
- File existence checking
- Dynamic file name generation
- Handling I/O failures gracefully

Full lab details are documented in LAB.md.

✅ License
This tool is shared for learning and demonstration purposes. Free to use and modify.
