#include<iostream>
using namespace std;
/*
--------------------------------------------------------
        Sabse Pahle To App Ne Ghabrana Nahi Hai
--------------------------------------------------------
*/
int main(){
    int ComputerGuess, userInput, attempt = 1; char consent;                                    // Declaring required Variables.
    ComputerGuess = (rand() % 10) + 1;                                                          // Taking Modulus of ComputerGuess with 10 so it gives a number in between 0 - 10.   Credit: ChatGPT
    cout<<"======================================="<<endl;                                      // Starting Banner of the Program. Nonthing much.
    cout<<"\tGarbage Guesser"<<endl;                                                            //
    cout<<"======================================="<<endl;                                      //
    cout<<"Can You Guess My Number?"<<endl;                                                     // Telling User About he has to guess the computer's number.
    do{
        cout<<"> "; cin>>userInput;                                                             // Again takes the input from user.
        if(userInput > ComputerGuess){                                                          // Checks if the user input is greter then the computer's number
        cout<<"[-] Your Input Is higher then Mine. Try Again!\t"<< "Attempt: "<<attempt + 1<<endl;  // Tell the user about its number is greter then the computer's number
        }
        else if(userInput < ComputerGuess){                                                     // Checks if the user input is less then the computer's number
            cout<<"[-] Your Input Is lesser then Mine. Try Again!\t"<< "Attempt: "<<attempt + 1<<endl;   // Tell the user about its number is greter then the computer's number
        }
        else {
            cout<<"======================================="<<endl;                                  // Winner Banner Msg
            cout<<"[+] You Guess It Right. Congratualtions ^_^"<<endl;                              //
            cout<<"======================================="<<endl;                                  //
            cout<<"Would You Like To Play Again. (y/n): ";                                          // Prompt the user about if he/she wants to play the game again or not?
            cin>>consent;                                                                           // Takes the user input
            switch (consent)                                                                        // Take the user input and enter in switch structure
            {
                case 'y':                                                                               // Match the user input charactor with "y","Y"
                case 'Y':                                                                               //
                cout<<"Ohh Shit! Here We Go Again."<<endl;                                          // Giving Some Msg
                main();                                                                             // Start The Main Function Again - This technique is called Recursion.
                return 0;                                                                           // End The Program
                break;                                                                              // Ending the Switch Body
            default:
                cout<<"\t\tGood Bye (-_;"<<endl;                                                        // Good Bye Msg
                return 0;                                                                           // End The Program
            }
        }
        ++attempt;
    }while (attempt <=3);
    cout<<"======================================="<<endl;                                          // User's Lost Banner
    cout<<"You Lost! My Number Is: "<<ComputerGuess<<endl;                                          // Showing the Computer's Number
    cout<<"======================================="<<endl;                                          //
    cout<<"Would You Like To Play Again. (y/n): ";                                                  // Prompt the user about if he/she wants to play the game again or not?
    cin>>consent;                                                                           // Takes the user input
    switch (consent)                                                                        // Take the user input and enter in switch structure
    {
        case 'y':                                                                           // Match the user input charactor with "y","Y"
        case 'Y':                                                                           //
        cout<<"Ohh Shit! Here We Go Again."<<endl;                                          // Giving Some Msg
        main();                                                                             // Start The Main Function Again - This technique is called Recursion.
    //cout<<"Segmentation Fault..."<<endl;
        return 0;                                                                           // End The Program
        break;                                                                              // Ending The Switch Body
    default:
        cout<<"Good Bye (-_;"<<endl;                                                        // Good Bye Msg
        return 0;                                                                           // End The Program
    }
    return 0;                                                                               // Good Practice
}