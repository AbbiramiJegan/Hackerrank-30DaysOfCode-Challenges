"""
This challenge involves reading a line of input, printing 'Hello, World.' on the first line, and then printing the input line on the second line.

Input:
- A single line of text which will be stored in a variable.

Output:
- Print 'Hello, World.' followed by the contents of the variable on separate lines.

Example:
Input:
Welcome to 30 Days of Code!

Output:
Hello, World.
Welcome to 30 Days of Code!

Explanation:
- The first line prints the string literal 'Hello, World.'.
- The second line prints the contents of the variable which, in this case, is 'Welcome to 30 Days of Code!'.
- This sequence ensures compliance with the expected output format specified in the challenge.
"""

# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)
