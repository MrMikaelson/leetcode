def exist_in_all(a, strs, index):
    for i in strs:
        if i[index] == a:
            continue
        else:
            return False
    return True


class Solution:
    def longestCommonPrefix(self, strs):
        lowest_length = len(strs[0])
        for i in strs:
            if len(i) < lowest_length:
                lowest_length = len(i)
        prefix = ""
        for i in range(lowest_length):
            char = strs[0][i]
            if exist_in_all(char, strs, i):
                prefix += char
            else:
                break

        return prefix


s = Solution()
print(s.longestCommonPrefix(["cir", "car"]))
