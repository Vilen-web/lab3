def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(num):
    primes = [n for n in num if is_prime(n)]
    return primes

nums = input()
numbers = [int(p) for p in nums.split()]
result = filter_prime(numbers)
print(result)
