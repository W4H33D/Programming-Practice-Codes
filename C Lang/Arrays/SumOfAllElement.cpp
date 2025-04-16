// Write A Program To Calculate Sum Of All Element Of Given Array.

#include <iostream>
using namespace std;

int main()
{
	int arr[] = {10, 100, 30, 400, 1002};
	int sum = 0;
	for(int i = 0; i < 5; i++)
	{
		sum += arr[i]; 
	}
	cout << "Sum Of All Element Of The Array: " << sum;
	return 0;
}