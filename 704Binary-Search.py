#Given an array of integers nums which is sorted in ascending order, and an integer target, 
#write a function to search target in nums. If target exists, then return its index. 
#Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        esq, dir = 0, len(nums) - 1 #inicializando as variaveis 
        
        while esq <= dir: #fazendo a busca binaria 
            
            meio = (esq + dir) // 2 
            
            if nums[meio] == target:
                return meio
            elif nums[meio] < target:
                esq = meio + 1
            else:
                dir = meio - 1
                
        return -1
            
     


