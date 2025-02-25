/*
A palindrome is a word (or other sequence of characters) that reads the same backward or forward.
Write a program that takes one word and prints its palindrome. You can use the for loop, the strlen function, and the %s format in scanf and print.
You can use a new variable or one declared earlier for holding the reversed value of a word.
Declare a string big enough to hold long words. For the record, you should use fgets instead of scanf in the future, especially when you want to have long strings with spaces.
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *palindrome(char *str)
{
    
    int len = strlen(str);
    // printf("[+] Length Of Array: %d\n", len);
    // printf("[+] Index Of Null Charactor is: %d\n", len - 1);
    char *ptr = (char*) malloc(len + 1);
    for(int i = 0; i < len; i++)
    {
        ptr[i] = str[(len - 1) - i];
    }
    ptr[len] = '\0';
    
    return ptr;
}

int main(void)
{
    char *rev;
    char word[20];
    printf("Enter A Word To Get Its Palindrome: ");
    scanf("%19s", word);
    rev = palindrome(word);
    printf("%s\n", rev);
    free(rev);

    return 0;
}