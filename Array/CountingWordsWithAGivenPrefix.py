class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count,l=0,len(pref)
        for word in words:
            if word[:l]==pref:
                count+=1
        return count