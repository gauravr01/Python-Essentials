def max_subarray_sum(arr):
    # Initialize variables to keep track of the current sum and the maximum sum
    current_sum = 0
    max_sum = 0
    
    # Iterate through the array
    for num in arr:
        # Update the current sum by adding the current number
        current_sum += num

        # If the current sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0
        # Update the max sum if the current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
        # TODO: Your code here
        
    # Return the maximum sum
    # TODO: Your code here
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print(result)
