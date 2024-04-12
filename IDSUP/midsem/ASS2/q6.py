def find_median(nums):
    nums.sort()
    print(nums)
    n = len(nums)
    if n % 2 == 0:
        # If the number of elements is even, average the two middle elements
        mid_left = n // 2 - 1
        mid_right = n // 2
        median = (nums[mid_left] + nums[mid_right]) / 2
    else:
        # If the number of elements is odd, the median is the middle element
        median = nums[n // 2]
    return median

# Example usage
nums = [5, 2, 9, 1, 5, 6]
print("List:", nums)
print("Median:", find_median(nums))