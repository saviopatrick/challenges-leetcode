#Given a string s consisting of words and spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      s = s.rstrip()
      palavra = s.split()
      ultima_palavra = palavra[-1]

      return len(ultima_palavra)