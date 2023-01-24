import math
class Solution:
    def searchInsert(self, nums, target):
            start = 0
            end = len(nums)-1
            middle = math.floor((start+end)/2)
            while not(nums[middle]==target) and start<=end:
                if target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1 
                middle = math.floor((start+end)/2)
            if nums[middle] == target:
                return middle
            else:
                return middle + 1