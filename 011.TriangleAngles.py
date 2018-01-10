"""
Triangle Angles

Most of the facets on a crystal are triangle. Since these crystals are vital to our base, we should attempt to learn more about this shape.

You are given the lengths for each side of a triangle. You need to find all three of the angles for this triangle. If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all angles as 0 (zero). The angles should be represented as a list of integers in ascending order. Each angle is measured in degrees and rounded to the nearest integer number using standard mathematical rounding.

Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.

Example:

angles(4, 4, 4) == [60, 60, 60]
angles(3, 4, 5) == [37, 53, 90]
angles(2, 2, 5) == [0, 0, 0]
Precondition:

0 < a ≤ 1000

0 < b ≤ 1000

0 < c ≤ 1000

"""
def angles(a, b, c):
    import math
    a1 = float(a)
    b1 = float(b)
    c1 = float(c)
    res = []
    try:
        t = (b1*b1+c1*c1-a1*a1)/(2*b1*c1)
        aa = int(round(math.acos(t)*(180.0/math.pi)))
        print(aa)
        t = (a1*a1+c1*c1-b1*b1)/(2*a1*c1)
        ba = int(round(math.acos(t)*(180.0/math.pi)))
        print(ba)
        ca = 180-aa-ba
        if ca>179:
            aa = 0
            ba = 0
            ca = 0
        res.append(aa)
        res.append(ba)
        res.append(ca)
        res.sort()
    except:
        res = [0,0,0]
    return res
