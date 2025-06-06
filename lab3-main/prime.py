def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

amount=int(input("Amount of numbers: "))
numbers = []

for i in range(amount):
    number = int(input({i+1}))
    numbers.append(number)

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)
