def find_second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least 2 elements"
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    if second_largest == float('-inf'):
        return "No second largest element found"
    
    return second_largest

# Example usage
numbers = [10, 20, 4, 45, 99]
result = find_second_largest(numbers)
print("Second largest number:", result)
