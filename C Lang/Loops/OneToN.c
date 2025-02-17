// Write a program that takes an integer N from the user and prints all numbers from 1 to N using a while loop.

#include<stdio.h>
void main(){
	int N;
	printf("Print A Number: ");
	scanf("%d", &N);
	int i = 1;
	while(i <= N){
		printf("%d\n", i);
		i++;
	}
}
