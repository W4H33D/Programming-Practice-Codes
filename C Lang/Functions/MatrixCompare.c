#include <stdio.h>

int compare_matrix(int * matrix1, int * matrix2, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            if (matrix1[i * cols + j] < matrix2[i * cols + j])
            {
                return -1;
            }
            else if (matrix1[i * cols + j] > matrix2[i * cols + j])
            {
                return 1;
            }
        }
    }
    return 0;
}

int print_Compare(int * matrix1, int * matrix2, int rows, int cols)
{
    int result = compare_matrix(matrix1, matrix2, rows, cols);
    if ( result == 1)
        printf("MatrixA is greater then MatrixB\n");
    else if (result == -1)
        printf("MatrixA is smaller then MatrixB\n");
    else
        printf("Both matrices are equal\n");
    return 0;
}

int main(void)
{
    int matrixA[3][3] = {
        {0, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int matrixB[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 19}
    };

    print_Compare((int*) matrixA, (int*) matrixB, 3, 3);
    return 0;
}
