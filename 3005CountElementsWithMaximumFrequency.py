#You are given an array nums consisting of positive integers.

#Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

#The frequency of an element is the number of occurrences of that element in the array.


class Solution:
  def maxFrequencyElements(self, nums : List[int]) -> int:
    aux = collections.Counter(nums)
    maximo = max(aux.values())

    cont = 0
    for i in nums:
      if aux[i] == maximo:
        cont +=1

    return cont
      
