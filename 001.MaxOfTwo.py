"""Max of Two

Define a function that takes two numbers as arguments and returns the largest of them.

Input: Two arguments as numbers.

Output: Maximum of two.

Example:

my_max(3, 3) == 3
my_max(0, 1) == 1
my_max(3, 2) == 3
"""

def my_max(a, b):
    if b > a:
        return b
    else:
        return a
