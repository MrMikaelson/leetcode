class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        l = len(words)
        for i in range(l-1,-1,-1):
            if len(words[i]) > 0:
                return len(words[i])