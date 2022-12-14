class Solution:
    def isPalindrome(self, x):
        num = str(x)
        for i in range(len(num)):
            if num[i] == num[-i-1]:
                continue
            else:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))
