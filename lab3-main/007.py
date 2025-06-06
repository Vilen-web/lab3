def has007(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

seven = input()
numbers = [int(num) for num in seven.split()]
result = has007(numbers)
print(result)
