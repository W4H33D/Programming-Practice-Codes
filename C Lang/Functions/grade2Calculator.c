#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        printf("Wrong parameters\n\n");
        printf("Usage: %s (add/sub/mul) int1 int2\n\nExample:\n%s add 3 2\n", argv[0], argv[0]);
        return 1;
    }

    int num1 = atoi(argv[2]);
    int num2 = atoi(argv[3]);

    if (strcmp(argv[1], "add") == 0)
    {
        printf("add %d %d: %d\n", num1, num2, num1 + num2);
    }
    else if (strcmp(argv[1], "sub") == 0)
    {
        printf("sub %d %d: %d\n", num1, num2, num1 - num2);
    }
    else if (strcmp(argv[1], "mul") == 0)
    {
        printf("mul %d %d: %d\n", num1, num2, num1 * num2);
    }
    else
    {
        printf("Wrong parameters\n\n");
        printf("Usage: %s (add/sub/mul) int1 int2\n\nExample:\n%s add 3 2\n", argv[0], argv[0]);
        return 1;
    }

    return 0;
}
