class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            left = 0
            j = i - 1
            while j >= 0:
                left += nums[j]
                j -= 1
            right = 0
            k = i + 1
            while k < len(nums):
                right += nums[k]
                k += 1
            out.append(abs(left-right))
        
        return out
        