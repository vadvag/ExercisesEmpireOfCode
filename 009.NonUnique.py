"""
Non Unique

If you have 50 different plug types, appliances wouldn't be available and
would be very expensive. But once an electric outlet becomes standardized,
many companies can design appliances, and competition ensues, creating variety
and better prices for consumers.

-- Bill Gates

You are given a non-empty list of integers (X). For this task, you should
return a list consisting of only the non-unique elements in this list. To do so
you will need to remove all unique elements (elements which are contained in a
given list only once). When solving this task, do not change the order of the
list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements so the result will
be [1, 3, 1, 3].

Input: A list of integers.

Output: The list of integers.

Example:

non_unique([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
non_unique([1, 2, 3, 4, 5]) == []
non_unique([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
non_unique([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

"""
def non_unique(lst):
    res = []
    l1 = list(set(lst))
    for i in lst:
        if type(i)==str:
            c = lst.count(i.upper())+lst.count(i.lower())
        else:
            c = lst.count(i)
        if c!=1:
            res.append(i)
    return res
