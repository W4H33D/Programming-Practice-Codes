#include<iostream>

using namespace std;

int avg(int arr[], int size)
{
    int sum = 0;
    for(int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum / size;
}

int main()
{
    int arr[5];
    for(int i = 0; i < 5; i++)
    {
        cout << "Enter Number " << i << ": ";
        cin >> arr[i];
    }
    cout << "Average Of All Elements: " << avg(arr, 5) << endl;
    
    return 0;
}