#include <stdio.h>

/*int i = 1;  int f = 1, feb = 1;
int fibo(int n){
    
    int temp = feb;
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
*/

int main()
{
	int f = 1, feb = 1;
	printf("%d\n", feb);
	for(int i = 1; i < 10; i++){
	    printf("%d\n", feb);
	    int temp = feb;
	    feb += f;
	    f = temp;
	}
	//fibo(100);
	return 0;
}

