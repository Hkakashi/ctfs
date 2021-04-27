#include <stdio.h>
#include <string.h>

void printFlagObfuscated(){
	printf("Successful!");
}

int main()
{
    int specialInt = 924053438;
    printf("Please enter a string: ");
    char buffer[11];
    gets(buffer);
    printf("specialInt: 0x%08x\n", specialInt);
    printf("specialInt: %i\n", specialInt);
    if(specialInt == 923992130){
        printFlagObfuscated();
    }else{
        printf("Input was %s. This is a very normal and boring program that prints your input.\n", buffer);
    }
    
    return 0;
}

