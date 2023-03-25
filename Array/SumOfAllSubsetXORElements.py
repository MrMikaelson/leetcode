import itertools

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # subsets = []
        s = 0
        for i in range(len(nums)+1):
            # subsets.extend(list(itertools.combinations(nums,i)))
            subsets = list(itertools.combinations(nums,i))
            for sub in subsets:
                xor = 0
                for i in sub:
                    xor = xor^i
                # print(s,xor)
                s+=xor
        return s