**Level of difficulty**: Medium

**Objectives**: Familiarize the student with:

- Working with files
- Reading from a file
- Writing to a file

**Scenario**
Write a program that will copy a file. However, if there is a destination file, then the program should try to create a new file (with a new file name) until the moment a destination file has been created.

| Remember to close both files.

> Note: in a real program, it's important to check whether all the files needed actually exist and that you can create a copy. In our program, creates "main.c" with some content, then copies it to a new file with a different name (e.g., "maincopy_1.c", "maincopy_2.c", and so on).

If the fopen function for the source file fails, then the program should print the message `Error opening file`. and end the program. If the process of creating a file fails, then you should change the name of the destination file.

You can append an integer number to the old file name.

Think about a limit on the number of attempts to create a file (it depends on your operating system and, of course, on the specific needs of your program). If you create too many files, it could be hard to use a directory that contains these files.

If your program has reached this limit (5), then it should print the message: `File count limit reached. and end the program`.

As you will notice, in the sandbox you cannot properly view the handling of the files that the sample solution modifies or generates, but you can try our code in your local development environment.

**Expected output**
```
Copy of the source file created: maincopy_1.c
```
