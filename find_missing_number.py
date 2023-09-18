def find_missing_number(nums):
    #length +1
    n = len(nums) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missing_number = total_sum - actual_sum
    return missing_number

    
result = find_missing_number([1, 2, 3, 5, 6, 7])
print(result)  # Output: 3