// Write a C++ program that takes a day number (1-7) as input and prints the corresponding day of the week using a switch statement.

#include<stdio.h>

void main()
{
	int day;
	printf("====================================\n");
	printf("\tWeek Day Name Guesser\n");
	printf("====================================\n");
	printf("\nEnter The Day Number To Guess: ");
	scanf("%d", &day);
	switch(day){
	case 1:
		printf("--> It is Monday\n");
		break;		
	case 2:
		printf("--> It is Tuesday\n");
		break;
	case 3:
		printf("--> It is Wednesday\n");
		break;
	case 4:
		printf("--> It is Thursday\n");
		break;
	case 5:
		printf("--> It is Friday\n");
		break;
	case 6:
		printf("--> It is Saturday\n");
		break;
	case 7:
	printf("--> It is Sunday\n");
		break;
	default:
		printf("[-] Invalid Week Day Number.\n");
	}
}
