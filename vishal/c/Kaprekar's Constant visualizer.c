/* Run in terminal: gcc "vishal/c/Kaprekar's Constant visualizer.c" -o "Kaprekar.exe"; .\Kaprekar.exe */
/*
 * Kaprekar's Constant Visualizer
 * This program demonstrates the process of reaching Kaprekar's constant (6174)
 * from any 4-digit number (with at least two different digits) using the Kaprekar routine.
 *
 * The constant is 6174. Any 4-digit number (with at least two different
 * digits) will reach 6174 within 7 steps using this process:
 *   1. Arrange digits in descending order  -> big number
 *   2. Arrange digits in ascending order   -> small number
 *   3. Subtract: big - small = new number
 *   4. Repeat until the number becomes 6174
 */

#include <stdio.h>

// Sort the 4 digits in descending order and return the number they form
int getDescending(int digits[4]) {
    int temp;
    // Simple bubble sort (descending)
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3 - i; j++) {
            if (digits[j] < digits[j + 1]) {
                temp = digits[j];
                digits[j] = digits[j + 1];
                digits[j + 1] = temp;
            }
        }
    }
    return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3];
}

// Sort the 4 digits in ascending order and return the number they form
int getAscending(int digits[4]) {
    int temp;
    // Simple bubble sort (ascending)
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3 - i; j++) {
            if (digits[j] > digits[j + 1]) {
                temp = digits[j];
                digits[j] = digits[j + 1];
                digits[j + 1] = temp;
            }
        }
    }
    return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3];
}

// Break a 4-digit number into its individual digits
void splitDigits(int number, int digits[4]) {
    digits[0] = (number / 1000) % 10;
    digits[1] = (number / 100) % 10;
    digits[2] = (number / 10) % 10;
    digits[3] = number % 10;
}

int main() {
    int number, step = 1;
    int digitsDesc[4], digitsAsc[4];

    printf("Kaprekar's Constant Finder\n");
    printf("Enter a 4-digit number (not all same digits): ");
    scanf("%d", &number);

    // Basic validation
    if (number < 1000 || number > 9999) {
        printf("Please enter a valid 4-digit number.\n");
        return 0;
    }

    int d[4];
    splitDigits(number, d);
    if (d[0] == d[1] && d[1] == d[2] && d[2] == d[3]) {
        printf("All digits are the same. Please try a different number.\n");
        return 0;
    }

    while (number != 6174) {
        // Get digits twice since sorting modifies the array
        splitDigits(number, digitsDesc);
        splitDigits(number, digitsAsc);

        int big = getDescending(digitsDesc);
        int small = getAscending(digitsAsc);
        int result = big - small;

        printf("Step %d: %d - %d = %d\n", step, big, small, result);

        number = result;
        step++;
    }

    printf("\nReached Kaprekar's Constant 6174 in %d steps!\n", step - 1);

    return 0;
}
