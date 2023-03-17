class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dupNums = nums.copy()
        dupNums.sort()
        less_dictionary = {}
        repeat = []
        for i in range(len(dupNums)):
            if dupNums[i] not in repeat:
                less_dictionary[dupNums[i]] = i
                repeat.append(dupNums[i])
        return [less_dictionary[i] for i in nums]