#include <errno.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{

    if(argc != 2)
    {
        printf("[-] Invalid Parameters\n");
        puts("Usage:\n--------");
        printf("\t%s <text-file>\n", argv[0]);
        printf("\nExample:\n---------\n");
        printf("\t%s example.txt", argv[0]);
        return 1;
    }
    FILE * src;
    int ch;
    int total_lines = 0, total_whitespace = 0, total_chars = 0;
    int small_letters[26] = {0};
    int upper_letters[26] = {0};
    char loop_lower = 'a';
    char loop_upper = 'A';

    if((src = fopen(argv[1],"rt")) == NULL) {
        fprintf(stderr,"Cannot open %s: %s\n",argv[1],strerror(errno));
        return 2;
    }

    while ((ch = fgetc(src)) != EOF) {
        total_chars++;
        if (ch == '\n') {
            total_lines++;
        }
        if (ch == ' ') {
            total_whitespace++;
        }

        if (ch >= 'a' && ch <= 'z') {
            small_letters[ch - 'a']++;
        }

        if (ch >= 'A' && ch <= 'Z') {
            upper_letters[ch - 'A']++;
        }
    }

    printf("Total Characters: %d\n", total_chars);
    printf("Total White Spaces: %d\n", total_whitespace);
    printf("Total Lines: %d\n", total_lines);
    for (int i = 0; i < 26; i++)
    {
        printf("| %c | %2d | %c | %2d |\n", loop_lower++, small_letters[i], loop_upper++, upper_letters[i]);

        if (loop_lower > 'z' || loop_upper > 'Z')
            break;
    }
    fclose(src);
    return 0;
}