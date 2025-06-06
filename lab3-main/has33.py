def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

three = input()
numbers = [int(num) for num in three.split()]
result = has33(numbers)
print(result)
