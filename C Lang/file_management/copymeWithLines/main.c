#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int size = 256;  // Default buffer size
    char *buffer;

    if (argc == 4) {
        size = atoi(argv[3]);
        if (size <= 0) {
            fprintf(stderr, "Invalid buffer size: %s\n", argv[3]);
            return 1;
        }
    } else if (argc != 3) {
        printf("\nUsage: %s <source file> <destination file> [buffer size]\n\n", argv[0]);
        printf("* Source file: The file from which content will be copied.\n");
        printf("* Destination file: The file into which the content will be copied.\n");
        printf("* Buffer size: The number of bytes used to read each line from the source file.\n");
        printf("               Note: If not specified, the default buffer size is 256.\n");
        fprintf(stderr, "Example:\n\t%s main.c copy.c 512\n", argv[0]);
        return 1;
    }

    buffer = (char *) malloc(size);
    if (buffer == NULL) {
        fprintf(stderr, "Cannot allocate buffer of size: %d\n", size);
        return 1;
    }

    FILE *src = fopen(argv[1], "rt");
    if (src == NULL) {
        fprintf(stderr, "Cannot open %s: %s\n", argv[1], strerror(errno));
        free(buffer);
        return 2;
    }

    FILE *dest = fopen(argv[2], "wt");
    if (dest == NULL) {
        fprintf(stderr, "Cannot write %s: %s\n", argv[2], strerror(errno));
        fclose(src);
        free(buffer);
        return 2;
    }

    for (int Lineno = 1; fgets(buffer, size, src) != NULL; Lineno++) {
        fprintf(dest, "%3d | %s", Lineno, buffer);
    }

    fclose(src);
    fclose(dest);
    free(buffer);
    return 0;
}
