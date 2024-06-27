"""
This challenge involves reading different types of input (integer, double, and string), performing specific operations, and printing the results in a formatted manner.

Input:
- An integer to be added to an initialized integer variable.
- A double value to be added to an initialized double variable.
- A string to be concatenated with another string that is already initialized.

Output:
- Print the sum of the integers on the first line.
- Print the sum of the doubles to one decimal place on the second line.
- Print the concatenated string on the third line.

Example:
Input:
12
4.0
is the best place to learn and practice coding!

Output:
16
8.0
HackerRank is the best place to learn and practice coding!

Explanation:
- The first integer input (12) is added to an existing integer variable.
- The second double input (4.0) is added to an existing double variable.
- The third string input is concatenated with a predefined string ('HackerRank ').
- Results are printed as specified, ensuring correct formatting and output.
"""

i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
int_num = 0
double_num = 0.0
str_word = ' '

# Read and save an integer, double, and String to your variables.
int_num = int(input())
double_num = float(input())
str_word = str(input())

# Print the sum of both integer variables on a new line.
print(i + int_num)

# Print the sum of the double variables on a new line.
print(d + double_num)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + str_word)