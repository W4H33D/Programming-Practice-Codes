void pfloydsTriangle(int size)
{
    int num = 1;
    for (int i = 1; i <= size; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (j == 0)
                printf("%d ", num++);
            else  if(num >= 100)
                printf("%4d", num++);
            else
                printf("%3d", num++);

        }
        printf("\n");
    }
}