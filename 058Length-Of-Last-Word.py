class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      s = s.rstrip()
      palavra = s.split()
      ultima_palavra = palavra[-1]

      return len(ultima_palavra)