#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same. 
#Then return the number of unique elements in nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        esq = 1

        for dir in range(1, len(nums)):
            if nums[dir] != nums[dir -1]:
                nums[esq] = nums[dir]
                esq += 1
        return esq