def rotate_array(arr, k):
    # Calculate the effective rotation index
    k = k % len(arr)
    
    # Rotate the array using slicing
    rotated_arr = arr[-k:] + arr[:-k]
    
    return rotated_arr
