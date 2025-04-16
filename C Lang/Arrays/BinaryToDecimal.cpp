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
            decimal += (1 << power);
        }
    }
    cout << "Decimal Number: " << decimal << endl;

    return 0;
}
