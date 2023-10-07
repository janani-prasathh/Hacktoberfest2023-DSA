#Find the Closest Pair from Two Sorted Arrays 
def closest_pair(arr1, arr2, target):
    min_diff = float('inf')
    pair = ()

    # Initialize pointers for the two arrays
    left = 0
    right = len(arr2) - 1

    while left < len(arr1) and right >= 0:
        current_sum = arr1[left] + arr2[right]
        current_diff = abs(current_sum - target)

        if current_diff < min_diff:
            min_diff = current_diff
            pair = (arr1[left], arr2[right])

        # Move pointers based on the comparison with the target
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return pair

# Example usage
arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
target = 32

result = closest_pair(arr1, arr2, target)
print("Closest pair:", result)
