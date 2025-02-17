/*
Write a program that asks for the IP address in a human readable form, creates three substrings, and prints them.

These substrings are created from parts 3, 2, and 1 of the last part of the IP address.

These substrings should be created with the use of pointers or array indexing (whichever you prefer). If a given string doesn't have three dots, then the program should print the message: Error: not a valid address..
*/

#include <stdio.h>

int main()
{
	char IpAddr[16]; // IP Address is only 15 charactors long but it takes one extra space to store "\0" at the end.
	int commaCount = 0;
	int commaIndex[3];
	char oct1[4]; char oct2[4]; char oct3[4]; char oct4[4];
	printf("> "); scanf("%15s", IpAddr);
	
	for(int i = 0; i < 16; i++){
	    if(IpAddr[i] == '.')
	        commaCount += 1;
	}
	if(commaCount != 3){
	    printf("Error: Not A Valid Address.\n");
	    return 1;
	}
	
	for(int i = 0, j = 0; i <= 15 && j < 3; i++){ // Getting Comma Index in IP Address String
	    if(IpAddr[i] == '.'){
	        commaIndex[j] = i;
	        j++;
	    }
	}

	if(commaIndex[0] >= 1 && commaIndex[0] <=3){
	    if((commaIndex[1] - commaIndex[0]) - 1 >= 1 && (commaIndex[1] - commaIndex[0]) - 1 <=3){
	        if((commaIndex[2] - commaIndex[1]) - 1 >= 1 && (commaIndex[2] - commaIndex[1]) - 1 <= 3){
	            int count = 0;
	            //int i = commaIndex[2];
	            for(int i = commaIndex[2]; (IpAddr[i+1]) != '\0'; i++){
	                ++count;
	            }
	            if(count >= 1 && count <= 3){
					int i;

					// Extract first octet
					for (i = 0; i < commaIndex[0]; i++) {
						oct1[i] = IpAddr[i];
					}
					oct1[i] = '\0'; // Null-terminate the string
				
					// Extract second octet
					for (i = 0; i < (commaIndex[1] - commaIndex[0] - 1); i++) {
						oct2[i] = IpAddr[commaIndex[0] + 1 + i];
					}
					oct2[i] = '\0';
				
					// Extract third octet
					for (i = 0; i < (commaIndex[2] - commaIndex[1] - 1); i++) {
						oct3[i] = IpAddr[commaIndex[1] + 1 + i];
					}
					oct3[i] = '\0';
				
					// Extract fourth octet
					for (i = 0; IpAddr[commaIndex[2] + 1 + i] != '\0' && i < 3; i++) {
						oct4[i] = IpAddr[commaIndex[2] + 1 + i];
					}
					oct4[i] = '\0';
	            }
	            else{
	                printf("\nError: Not A Valid Address.\n");
	                return 1;
	            }
	        }
	        else{
	            printf("Error: Not A Valid Address.\n");
	            return 1;
	        }
	    }
	    else{
	        printf("Error: Not A Valid Address.\n");
	        return 1;
	    }
	}
	else{
	    printf("Error: Not A Valid Address.\n");
        return 1;
	}

	printf("Last 3 parts: %s.%s.%s\n", oct2,oct3,oct4);
	printf("Last 2 parts: %s.%s\n", oct3,oct4);
	printf("Last 1 parts: %s\n", oct4);
	return 0;
}