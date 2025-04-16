#include<iostream>

using namespace std;

int main()
{
    char word[20];
    cout << "Enter A Word: ";
    cin >> word;
    cout << "Echo: " << word << endl;
    for(int i = 0; word[i] != '\0'; i++)
    {
        cout << word[i] << " ";
    }
    // cin.getline(word, 20);
    return 0;
}
