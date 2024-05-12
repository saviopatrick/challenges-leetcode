#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
#The order of the elements may be changed. 
#Then return the number of elements in nums which are not equal to val.



class Solution:
    def removeElement(self, nums, val):
        i = 0  

        for j in range(len(nums)):
            if nums[j] != val:
            
                nums[i] = nums[j]
                i += 1  

        return i 
