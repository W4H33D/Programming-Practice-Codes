#include <stdio.h>
#include "itriangle.h"

int main(void)
{
    int size;
    printf("Enter the size of triangles: ");
    scanf("%d", &size);

    printf("Backslash Triangle:\n");
    prightTriangle(size);
    printf("Floyd's Triangle:\n");
    pfloydsTriangle(size);
    return 0;
}