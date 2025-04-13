/*
       Write a program that displays the multiplication table of a given size.
       
       First, your program should ask the user to specify the size (height and weight are equal, so one number should be enough).
       
       If the size is greater than 20, the program should print the message: Matrix too big..
       
       Then it should allocate a matrix and fill this matrix with appropriate values (remember: the element of [0][0] should store the multiplication result of 1 and 1).
       
       Then the program should print the multiplication table, four characters per cell. Finally, all memory must be freed.
       
       Your version of the program must print the same result as the expected output.
       
       Sample input
       5
       
       Expected output
              1   2   3   4   5
          1   1   2   3   4   5
          2   2   4   6   8  10
          3   3   6   9  12  15
          4   4   8  12  16  20
          5   5  10  15  20  25
       
       Sample input
       25
       
       Expected output
       Matrix too big.
*/

#include<stdio.h>
#include<stdlib.h>
int main()
{
       int size;
       int** matrix;
       printf("Enter The Size of Multiplication Table: ");
       scanf("%d", &size);
       if (size > 20)
       {
              printf("Multiplication Table Cannot Be Greater Then 20\n");
              return 1;
       }

       // Assinging Matrix Size which contains Pointers.
       matrix = (int**) malloc(size * sizeof(int*));
       

       if (matrix == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
       }

       // Assinging "Pointer To Int" Value to each Poiter Index of Matrix 
       for (int i = 0; i < size; i++) 
       {
              matrix[i] = (int *)malloc(size * sizeof(int));
              if (matrix[i] == NULL)
              {
              printf("Memory allocation failed!\n");
              return 1;
              }
       }

       // Putting Values of Multiplication table in the Matrix
       for (int i = 0; i < size; i++) 
       {
              for (int j = 0; j < size; j++) 
              {
                     matrix[i][j] = (i + 1) * (j + 1);
              }
       }
       


       // Matrix Builder Loop
       // ===================

       for(int i = 1; i <= size; i++)
              printf("\t%d", i);
       for(int i = 0; i < size; i++)
       {
              printf("\n%d\t", i+1);
              for(int j = 0; j < size; j++)
              {
                     printf("%d\t", matrix[i][j]);
              }
       }

       //  Free memory
       for (int i = 0; i < size; i++) 
       {
           free(matrix[i]); // free each row
       }
       free(matrix); // free the array of row pointers
       return 0;
}
