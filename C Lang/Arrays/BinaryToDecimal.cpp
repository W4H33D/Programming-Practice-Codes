#include<iostream>
#include<cstring>

using namespace std;

int main() {
    char binary[20];
    int decimal = 0;

    cout << "Enter a Binary Number: ";
    cin >> binary;

    int len = strlen(binary);

    for (int i = 0; i < len; i++) {
        if (binary[i] == '1') {
            int power = len - i - 1;
            int value = 1;
            // Calculate 2^power manually
            for (int j = 0; j < power; j++) {
                value *= 2; // Multiply by 2 for each power
            }
            decimal += value; // Add the value to the decimal
        }
    }

    cout << "Decimal Number: " << decimal << endl;

    return 0;
}
