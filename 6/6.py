'''
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def square_of_sum(n):
    sum = ((n+1)*n)/2
    squared = sum**2
    return squared
 
def sum_of_squares(n):
    sum = 0
    for i in range(n + 1):
        sum += i**2
    return sum

n = 100 
 
print square_of_sum(n) - sum_of_squares(n)

'''

initial solution
    
sum_squares = 0

for i in range(1, 101):
    sum_squares = sum_squares + (i * i)

sum = 0

for i in range(1, 101):
    sum = sum + i

sum_square = sum * sum

print sum_square - sum_squares

'''