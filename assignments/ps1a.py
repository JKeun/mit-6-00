n = int(input("Which prime number do you wnat to know? "))
state = 0
number = 2

while state < n:
    if number % 2 == 1:  # if odd
        divisor = 2
        count = 0
        while divisor < number:
            if number % divisor == 0:
                count = count + 1
            divisor = divisor + 1
        if count == 0:  # if number has no remainder -> prime
            prime = number
            state = state + 1
    elif number == 2:  # if 2 -> prime
        prime = number
        state = state + 1
        
    number = number + 1

print("state: ", state)
print("prime: ", prime)
