class Solution:
    def palindrome(self,s):
        for i in range(len(s)//2):
            if s[i] != s[- 1 - i]:
                return False
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.palindrome(word):
                return word
        return ""