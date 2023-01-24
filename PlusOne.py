class Solution:
    def increment(self,i,digits):
        if digits[i] == 9:
            digits[i] = 0
            if i == -len(digits):
                digits.insert(0,1)
                return digits
            if digits[i-1] != 9:
                digits[i-1] += 1
                return digits
            else:
                return self.increment(i-1,digits)
    def plusOne(self, digits):
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            return self.increment(-1,digits)