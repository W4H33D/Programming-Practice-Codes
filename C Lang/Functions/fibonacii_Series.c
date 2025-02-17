// Fibonacii Series Using Function Recursion

#include <stdio.h>
long int i = 1; long int f = 1, feb = 1;
int fibo(int n){
    
    long int temp = feb;
    if(i < n){
        printf("%d\n", feb);
	    temp = feb;
	    feb += f;
	    f = temp;
	    i++;
	    fibo(n);
    }
    else
        return 1;
    
}
int main()
{
	/*
	int f = 1, feb = 1;
	printf("%d\n", feb);
	for(int i = 1; i < 10; i++){
	    printf("%d\n", feb);
	    int temp = feb;
	    feb += f;
	    f = temp;
	}
	*/
	fibo(25);
	return 0;
}

