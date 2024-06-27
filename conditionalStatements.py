"""
Determines if a given integer is "Weird" or "Not Weird" based on specific conditions.

- If the integer is odd, print "Weird".
- If the integer is even and in the inclusive range of 2 to 5, print "Not Weird".
- If the integer is even and in the inclusive range of 6 to 20, print "Weird".
- If the integer is even and greater than 20, print "Not Weird".

Args:
    n (int): A positive integer.

Returns:
    None

Example:
    For n = 3, output is "Weird".
    For n = 24, output is "Not Weird".
"""

def conditional(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

N = 7
conditional(N)