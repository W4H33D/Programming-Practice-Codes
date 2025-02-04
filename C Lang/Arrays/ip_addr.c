#include <stdio.h>

int main()
{
	char oct1[3];
	char oct2[3];
	char oct3[3];
	char oct4[3];
	char IP[15];
	
	printf("Enter The IP Address:-\n");
	printf("> "); scanf("%3s %3s %3s %3s", oct1,oct2,oct3,oct4);
	sprintf(IP, "%s.%s.%s.%s\n", oct1,oct2,oct3,oct4);
	/*
	    sprintf --> Syntax:
	       sprintf(Char_Array_Identifier,"String You want to store in Char_Array", No_of_Variables_Here);
	*/
	printf("%s", IP);
	return 0;
}
