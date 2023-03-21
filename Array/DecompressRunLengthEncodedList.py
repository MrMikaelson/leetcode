class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)//2):
            out.extend([nums[2*i+1]]*nums[2*i])
        return out