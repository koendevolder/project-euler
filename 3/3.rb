=begin
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
=end

n = 600851475143
i = 2

while n != i
    while n % i == 0
        n = n / i
    end
    i = i + 1
end

puts n