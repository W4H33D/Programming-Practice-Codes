// Write a C++ function that takes an integer as input and returns its factorial. Call this function from main() and display the result.
// factorial = n(n-1)(n-2)(n-3)....1
#include<stdio.h>

int factorial(int a){
	int temp = 1;
	for(int i = a; i >= 1; i--){
		temp *= i;
	}
	return temp;
}

void main()
{
	int fact;
	printf("Enter A Number To Calculate Factorial: ");
	scanf("%d", &fact);
	printf("Factorial = %d",factorial(fact));
}

