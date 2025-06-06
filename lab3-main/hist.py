def histogram(numbers):
    for num in numbers:
        print("*" * num)

numbers = input()
hist = [int(num) for num in numbers.split()]
histogram(hist)