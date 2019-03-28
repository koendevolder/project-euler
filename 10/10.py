'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

limit = 2000000
limitn = limit + 1
primes = dict()

for i in range(2, limitn):
    primes[i] = True

for i in primes:
    factors = range(i, limitn, i)
    for f in factors[1:]:
        primes[f] = False

print sum(i for i in primes if primes[i]==True)

'''

solution 1

a = range(2, 2000000)
i = 0

while i < len(a):
    j = i + 1
    while j < len(a):
        if (a[j] % a[i] == 0):
            a.pop(j)
        j = j + 1
    i = i + 1

print sum(a)

solution 2

limit = 2000000
a = range(2, limit)
i = 0

while i < len(a):
    j = a[i]**2
    k = a[i]
    while j < limit:
        try:
            a.pop(a.index(j))
        except ValueError:
            pass
        j = j + k
    i = i + 1

print sum(a)


'''