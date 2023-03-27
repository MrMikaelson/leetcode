class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cD = {}
        for num in nums:
            if num not in cD:
                cD[num] = 1
            else:
                cD[num] += 1
        return [sum([i//2 for i in cD.values()]),sum([i%2 for i in cD.values()])]