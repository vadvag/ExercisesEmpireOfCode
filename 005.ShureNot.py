"""
Sure Not

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

Input: String.

Output: Changed string.

Example:

sure_not("sure") === "not sure"
sure_not("not sure") === "not sure"
sure_not("noter") === "not noter"
"""

def sure_not(line):
    if line.find("not ") == -1:
        line = "not "+line
    return line
