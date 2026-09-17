def reverse_list(nums):
    left, right = 0, len(nums)-1
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


numbers = [1, 2, 3, 4, 5, 6]
print(reverse_list(numbers))
