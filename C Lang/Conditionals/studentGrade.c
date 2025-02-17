/*
Write a C++ program that takes a student's marks as input and prints their grade based on the following
conditions:
90 and above → A+
80 - 89 → A
70 - 79 → B
60 - 69 → C
Below 60 → Fail
*/
#include<stdio.h>

void main(){
    int marks;
    printf("=========================================\n");
    printf("\tStudent Grade Calculator\n");
    printf("=========================================\n\n");
    printf("Enter Your marks Persentage: ");
   
    scanf("%d", &marks);
    if(marks >= 90){
        printf("Congratulations! Your Grade is A+\n");
    }
    else if (marks >80 && marks <= 89){
        printf("Congratulations! Your Grade is A\n");
    }
    else if (marks > 70 && marks <= 79){
        printf("Congratulations! Your Grade is B\n");
    }
    else if (marks >= 60 && marks <= 69){
        printf("Congratulations! Your Grade is C\n");
    }
    else{
        printf("Your Grade is \'F\'. Try Again");
    }
    
}
