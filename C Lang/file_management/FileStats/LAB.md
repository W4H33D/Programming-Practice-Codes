### LAB

**Level of difficulty:** Medium

**Objectives:** Familiarize the student with:
- Working with files
- Reading from a file
- Simple data processing
- Loop over file content

### Scenario
Write a program that counts the metrics of a file:

1. Number of all characters
2. Number of whitespaces 
3. Number of lines 
4. Number of all lower-case letters

You can (for now, to simplify your task, of course) assume constant file names. To speed up your programming, you can test your program on its source code. First, open a file in read mode. After that, character by character, read the file and count the numbers asked. Remember to close the file.

> Note: in a real program, it's important to check whether all the files needed actually exist and that you can read their contents. In our program, you should at least check that the files have been successfully opened.

If the `fopen` function fails, then print the message `Error opening file`. and end the program. There's only one instance of output from your program - your output can vary, depending on the file contents.

Your code can be based on the sample solution, which serves two purposes, the creation of a file and its subsequent analysis. The program showcases basic `file creation`, `writing`, and `reading` operations in C, along with a simple analysis of the file content, counting `characters`, `whitespaces`, `lines`, and occurrences of `small letters`.


**Expected output**
```
Lines: 14
Whitespaces: 192
Characters: 1154
Small letter: a : 81
Small letter: b : 17
Small letter: c : 26
Small letter: d : 36
Small letter: e : 122
Small letter: f : 23
Small letter: g : 31
Small letter: h : 58
Small letter: i : 63
Small letter: j : 1
Small letter: k : 6
Small letter: l : 52
Small letter: m : 19
Small letter: n : 65
Small letter: o : 55
Small letter: p : 15
Small letter: q : 3
Small letter: r : 56
Small letter: s : 51
Small letter: t : 89
Small letter: u : 11
Small letter: v : 11
Small letter: w : 16
Small letter: x : 0
Small letter: y : 20
Small letter: z : 1
```