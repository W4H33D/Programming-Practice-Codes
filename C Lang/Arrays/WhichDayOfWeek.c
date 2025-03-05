/*
Write a program that asks the user to enter a number, and prints which day of the week that number corresponds to. The days are indexed from 0 (Sunday) to 6 (Saturday).

Store the names of the days in an array and print the name of the day in two ways:

with pointer arithmetic;
with array indexing.
Before the program gets a value from the array, it must first check if the given day is greater than or equal to zero and less than 7. If not, it should print the message: Error, no such day..

```hint
	0			1			2			3		  4			5			6
	|			|			|			|		  |			|			|
[ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
```
*/
#include <stdio.h>

int main()
{
	char days[7][10] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

	int userInput;
	printf("Enter The Day Number [0-6]: ");
	scanf("%d", &userInput);
	
	if(userInput < 0 || userInput > 6){
		printf("Error, No Such Day Number In My World. Maybe Mars Have!\n");
		return 0;
	}
	
    printf("Pointer Version: %s\n", *(days + userInput));
	printf("Array Index Version: %s", days[userInput]);


	return 0;
}