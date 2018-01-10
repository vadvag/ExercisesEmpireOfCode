"""
Fizz Buzz

To get them ready for storage, we need the worker-bots to sort crystals by 3
or 5 or divide them by the number of edges. To make things easier, we will base
our program on the ancient human word game "Fizz buzz".

Our goal is to write a function that will receive a positive integer and
return:

The phrase "Fizz Buzz" if the number is divisible by 3 and by 5,

The word "Fizz" if the number is divisible by 3,

The word "Buzz" if the number is divisible by 5,

The number as a string for all other cases.

Input: A number as an integer.

Output: The answer as a string.

Example:

fizz_buzz(15) == "Fizz Buzz"
fizz_buzz(6) == "Fizz"
fizz_buzz(5) == "Buzz"
fizz_buzz(7) == "7"
"""
def fizz_buzz(number):
    res=""
    if number%3==0:
        res = res+"Fizz"
        
    if number%5==0:
        if res != "":
            res=res+" "
            
        res=res+"Buzz"
    if res=="":
        res = str(number)
    return res
