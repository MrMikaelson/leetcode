class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        out = 0
        for i in range(len(nums)//2):
            out += nums[2*i]
        return out