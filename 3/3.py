'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

n = 600851475143
i = 2

while n != i:
    while n % i == 0:
        n = n / i
    i = i + 1

print n

'''
def prime_number (var):
    for i in range(2, var):
        if (var % i == 0):
            return False
            break  
    return True

---

initial solution

n = 600851475143
i = 2

while n != i:
    if (n % i == 0):
        n = n / i
        i = 2
    i = i + 1

print n

---

internet solution

n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print n
'''