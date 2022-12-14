def removeDuplicates(nums):
        k = 0
        for i in range(1,len(nums)):
            if nums[k] == nums[i]:
                nums[k] = nums[i]
            else:
                nums[k+1] = nums[i]
                k = k+1
        return k+1

nums = [1,2,2,3]
removeDuplicates(nums)
print(nums[:removeDuplicates(nums)])