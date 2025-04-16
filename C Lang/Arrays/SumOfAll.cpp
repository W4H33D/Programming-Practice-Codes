#include<iostream>

using namespace std;

int sum(int *arr, int size)
{
    int sum = 0;
    for(int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}

int main()
{
    int arr[5];
    for(int i = 0; i < 5; i++)
    {
        cout << "Enter Number " << i << ": ";
        cin >> arr[i];
    }
    cout << "Sum Of All Elements: " << sum(arr, 5) << endl;
    
    return 0;
}