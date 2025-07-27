#include <stdio.h>

int main(int argc, char * argv[])
{
    if (argc < 2)
    {
        printf("Invalid parameters supplied\n");
        printf("Usage: %s <source file>\n", argv[0]);
        return 1;
    }

    FILE *src, *dest;
    char filename[50];
    int ch;

    if ((src = fopen(argv[1], "rb")) == NULL)
        {
        printf("Error opening file.\n");
        return 1;
    }

    int success = 0;
    for (int i = 1; i <= 5; i++) {
        snprintf(filename, sizeof(filename), "maincopy_%d.c", i);
        if ((dest = fopen(filename, "r")) == NULL) {  // file doesn't exist
            dest = fopen(filename, "wb");  // create it
            success = 1;
            break;
        }
    }
    if (!success) {
        printf("File count limit reached.\n");
        fclose(src);
        return 1;
    }


    while ((ch = fgetc(src)) != EOF) {
        fputc(ch, dest);
    }

    printf("Copy of the source file created: %s", filename);

    fclose(src);
    fclose(dest);
    return 0;
}