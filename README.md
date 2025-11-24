# Student CGPA Calculator

## Overview
The Student CGPA Calculator is a Python-based console application designed to assist students in calculating their Cumulative Grade Point Average (CGPA).By inputting individual grades and their corresponding credit weights, the system computes the weighted average to provide an accurate academic performance metric.

## Features
* Weighted Calculation: accurately calculates CGPA by multiplying grades by their respective credits and dividing by total credits.
* Dynamic Input: Allows the user to specify the number of subjects they wish to enter for each calculation.
* Data Summary: Displays a list of entered grades, credits, and the sum of total credits before showing the final result.
* Error Handling: Includes logic to handle scenarios where total credits are zero to prevent division by zero errors.
* Interactive Loop: Users can perform multiple calculations in a single session without restarting the program via a "Do you wish to calculate any more" prompt.

## Technologies/Tools Used
* Language: Python 3
* Libraries: Standard Python I/O 

## Steps to Install & Run the Project
1.  Prerequisites: Ensure you have Python installed on your machine. You can check this by running "python version" in your terminal.
2.  Download: Save the file "source-code.py" to a local directory.
3.  Execution:
    * Open your terminal or command prompt.
    * Navigate to the directory containing the file.
    * Run the following command:
       " python source-code.py"
        
## Instructions for Testing
To verify the application is working correctly, follow these steps:

1.  Launch: Start the application using the command above.
2.  Input Count: When prompted "Enter the number of grades and credits", enter "2".
3.  Subject 1:
    * Enter grade mark: "9.0"
    * Enter credit: "3"
4.  Subject 2:
    * Enter grade mark: "8.0"
    * Enter credit: "4"
5.  Verify Output:
    * The system should display: "Total Credits: 7"
    * The calculated CGPA should be approximately: "8.42" (Calculation: $((9*3) + (8*4)) / 7$).
6.  Loop Test: When asked "Do you wish to calculate any more CGPA(y/n)", enter "n" to exit or "y" to run another test case.
