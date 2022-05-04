# package fsearch

# Implement linear_search here
# Time complexity O(n)
def linear_search(nums, target):
    for i in range(len(nums)):
        if i == target:
            return i
    return -1    

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
