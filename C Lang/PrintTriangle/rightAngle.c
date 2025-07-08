//
// Created by waheed on 7/7/2025.
//
#include <stdio.h>
void prightTriangle(int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("\\");
        }
        puts("");
    }
}