"""Crystal Row

A crystal or crystalline solid is a solid material whose constituents, such as
atoms, molecules or ions, are arranged in a highly ordered microscopic structure,
forming a crystal lattice that extends in all directions. The scientific
definition of a "crystal" is based on the microscopic arrangement of atoms
inside it, called the crystal structure. A crystal is a solid where the atoms
form a periodic arrangement.

Because crystals are such an important resource, systems must be put in place
to check the crystal quality during the growth and harvest periods. For our
initial tests, we use random spot checks on the atomic lines composing each
of the crystals. This crystal type contains two atoms composed of the elements
"X" (Xenatom) and "Z" (Zorium). In a well grown crystal, these atoms should
alternate down the atomic line.

You are given a random atomic line from a sample crystal lattice as a sequence
of the letters "X" and "Z". A good line should have the periodic arrangement
(one by one) looking like ["X", "Z", "X", "Z"]. If any atoms neighbor another
of the same element, then this crystal is of no use to us and should be
discarded.

X - Z - X - Z - X - Z Good
Z - X - Z - X - Z - X Good
Z - X - X - Z - X - Z Bad
Z - X - Z - Z - Z - X Bad

Input: Atomic lines as a list of strings.

Output: The crystal quality as a boolean.

Example:

checkLine(["X", "Z", "X"]) == true
checkLine(["X", "Z", "X", "X"]) == false
Precondition:

1 < |line| ≤ 1000

∀ x ∈ line: x='X' OR x='Z'

"""

def check_line(line):
    res = True
    ver = ""
    for i in line:
        if i == ver:
            res = False
        ver = i    
    return res
