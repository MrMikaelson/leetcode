def checkEquality(i,needle,haystack):
    if haystack[i:i+len(needle)] == needle:
        return True
    else:
        return False

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i = haystack.index(needle[0])
            deleted = 0
            while not checkEquality(i,needle,haystack):
                haystack = haystack[i+1:]
                deleted+=(i+1)
                i = haystack.index(needle[0])
            return i+deleted
        else:
            return -1