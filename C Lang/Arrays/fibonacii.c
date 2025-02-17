// Fibinacii Series Using arrays

#include <stdio.h>

int main()
{
	long int fiboArr[10] = {1};
	for(int i = 1; i < 10; i++){
	    fiboArr[i] = fiboArr[i-2]+fiboArr[i-1];
	}
	for(int i = 0; i < 10; i++){
	    printf("%d\n", fiboArr[i]);
	}
	
	return 0;
}

