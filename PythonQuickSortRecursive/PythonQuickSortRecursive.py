import sys

def quickSort(nums: list) -> list:
    if(len(nums) <= 1):
        return nums
    else:
        return (
            quickSort([el for el in nums[1:] if el <= nums[0]])
            + [nums[0]]
            + quickSort([el for el in nums[1:] if el > nums[0]])
            )

nums = [5,4,3,2,1]
print(quickSort(nums))


