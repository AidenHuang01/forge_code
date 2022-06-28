# package fsort

# Implement bobble sort





def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def quick_sort(nums):
    def sort(nums, left, right):
        if len(nums) == 1 or left >= right:
            return nums
        pivot = partition(nums, left, right)
        sort(nums, left, pivot - 1)
        sort(nums, pivot + 1, right)
        return nums
    def partition(nums, left, right):
        pivot = nums[right]
        ptr = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1
        nums[ptr], nums[right] = nums[right], nums[ptr]
        return ptr
    return sort(nums, 0, len(nums) - 1)
    