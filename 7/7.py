'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

a = range(2, 110000)
i = 0

while i < (10001-2):
    j = i + 1
    while j < len(a):
        if (a[j] % a[i] == 0):
            a.pop(j)
        j = j + 1
    i = i + 1

print a[i]