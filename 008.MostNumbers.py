"""
Most Numbers

To check an automated sieve for ore we use a variety of sample sets to find the
smallest and the largest stones. The difference between these values is then
used to decide if the sample is worth checking.

You are given an array of numbers from which you must find the difference
between the maximum and minimum elements. Your function should be able to
handle an undefined amount of arguments. For an empty argument list, the
function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary)
fractions, since this is the case, we should check that the result is within
0.001 precision.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between the maximum and minimum as a number (int, float).

Example:

most_difference(1, 2, 3) == 2
most_difference(5, -5) == 10
most_difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
most_difference() == 0
Precondition:

0 ≤ |arguments| ≤ 20
"""

def most_difference(*args):
    lst = []
    for ar in args:
        lst.append(ar)
    ret = 0
    if len(lst) != 0:
        ret = max(lst)-min(lst)
    return ret
