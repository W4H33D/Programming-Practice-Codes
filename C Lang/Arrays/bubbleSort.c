#include <stdio.h>

int main()
{
	float numbers[10] = {5.6, 4.3, 6.2, 6.4, 7.3, 2.3, 8.3, 9.2, 0.1, 1.9};
	float temp;
	int isSwaped;
	do{
	    isSwaped = 0;
	    for(int i = 0; i < 9 /*10*/; i++){
	        if(numbers[i] > numbers[i + 1]){
	            isSwaped = 1;
	            temp = numbers[i];
	            numbers[i] = numbers[i + 1];
	            numbers[i + 1] = temp;
	        }
	    }
	    
	    for(int ii = 9; ii >= 0; ii--){
	        printf("%.2f ", numbers[ii]);
	    }
	    printf("\n");
    }while(isSwaped);
	//puts("Sorted Array: ");
	return 0;
}
