'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

perimeter = 1000

for a in range (1, perimeter + 1):
    for b in range (1, perimeter + 1):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print a * b * c
                
'''

initial solution
    
for a in range (1001):
    for b in range (1001):
        c = (a**2.0 + b**2.0)**(1.0/2.0)
        if c == int(c):
            if a + b + c == 1000:
                print a * b * c
'''