'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers. 
'''

import sys

for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        num = i * j
        if str(num) == str(num)[::-1]:
            print num
            print i
            print j
            sys.exit()


'''
initial solution

import sys

def palindrome(var):
    var = str(var)
    for i in range(0,len(var)/2):
        if (var[i] != var[len(var)-1-i]):
            return False
    return True

for i in range (999, 900, -1):
    for j in range (999, 900, -1):
        if palindrome(i * j):
            print i * j 
            print i
            print j
            sys.exit()
'''