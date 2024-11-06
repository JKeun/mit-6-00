from math import *

# number theory
# n = 6
# 2 * 3 * 5 ~~ e**6
# log(2) + log(3) + log(5) ~~ 6

n = int(input("What is n? "))
number = 2
sum_log_prime = 0

while number < n:
    prime = 1
    if number % 2 == 1:  # if odd
        divisor = 2
        count = 0
        while divisor < number:
            if number % divisor == 0:
                count = count + 1
            divisor = divisor + 1
        if count == 0:  # if number has no remainder -> prime
            prime = number
    elif number == 2:  # if 2 -> prime
        prime = number
        
    sum_log_prime = sum_log_prime + log(prime)
    number = number + 1

print("sum of the logs of the primes: ", sum_log_prime)
print("n: ", n)
print("rator of these two quantities: ", sum_log_prime / n)
