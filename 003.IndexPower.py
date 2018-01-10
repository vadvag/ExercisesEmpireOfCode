"""
Index Power

Each level of the mine requires energy in exponential quantities for each device. Hmm, how to calculate this?

You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:

array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
Input: An array as a list of integers and a number as an integer.

Output: The result as an integer.

Example:

index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1
Precondition:

0 < |array| ≤ 10

0 ≤ N

∀ x ∈ array: 0 ≤ x ≤ 100
"""

def index_power(array, n):
    if n < 0 or n>100:
        res = -1
    elif n == 0:
        res = 1
    else:    
        if len(array) < n+1:
            res = -1
        else:
            zn = array[n]
            res = 1
            for i in range(n):
                res = res*zn
    return res
