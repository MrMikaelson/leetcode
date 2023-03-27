class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = ['a','e','i','o','u']
        out = 0
        for word in words[left:right+1]:
            if (word[0] in vowels) and (word[-1] in vowels):
                out += 1
        return out