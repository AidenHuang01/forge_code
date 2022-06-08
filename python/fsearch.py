# package fsearch

# Implement linear_search here
# Time complexity O(n)
def linear_search(nums, target):
    for i in range(len(nums)):
        if i == target:
            return i
    return -1    

def binary_search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


