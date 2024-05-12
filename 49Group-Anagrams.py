#Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupo = {}

        for i in strs:
            palavra = ''.join(sorted(i))
            if palavra not in grupo:
                grupo[palavra] = [i]
            else:
                grupo[palavra].append(i)  

        return [*grupo.values()]
