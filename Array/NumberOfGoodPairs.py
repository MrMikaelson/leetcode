class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        for i in nums:
            if i in repeat:
                repeat[i]+=1
            else:
                repeat[i]=1
        num = 0
        for i in repeat:
            if repeat[i]>1:
                num+=(repeat[i]*(repeat[i]-1)//2)
        return num