# Pyramid

## Project Description
This project is a simple command-line program that prompts the user to enter a height and builds a pyramid of that height using the `#` character. The program ensures the height is between 1 and 8, inclusive.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Code Explanation](#code-explanation)

## Installation
No special installation is required for this project. Ensure you have Python and the CS50 library installed.

## Usage
To run the project, use the following command:
```bash
python pyramid.py
```
The program will prompt you to enter the desired height of the pyramid (between 1 and 8).

## Algorithm Explanation
The algorithm works as follows:

### Get Valid Height:
The program prompts the user to enter the height of the pyramid.
It ensures the height is between 1 and 8, inclusive.
### Build the Pyramid:
The program builds the pyramid row by row.
Each row consists of spaces followed by # characters to form the desired pyramid shape.
## Code Explanation
Importing the CS50 Library
``` python

from cs50 import get_int
```
This imports the get_int function from the CS50 library, which is used to get integer input from the user.

Get Input Function
``` python

def get_input():
    while True:
        x = get_int("enter the desired height: ")
        if x > 0 and x <= 8:
            return x
        else:
            return get_input()
```
Prompts the user to enter the desired height of the pyramid.
Ensures the height is between 1 and 8, inclusive.
Returns the valid height.
Main Logic
``` python

height = get_input()

for rows in range(height):
    for spaces in range(height - rows - 1):
        print(" ", end="")
    for blocks in range(rows + 1):
        print("#", end="")
    print()
```
Calls the get_input function to get the valid height of the pyramid.
Builds the pyramid row by row.
For each row, it prints the required number of spaces followed by the required number of # characters.
Uses nested loops to control the number of spaces and # characters.
The print() function with end="" ensures the characters are printed on the same line.
