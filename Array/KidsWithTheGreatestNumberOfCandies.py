class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        greatest = max(candies)
        for i in candies:
            if i + extraCandies >= greatest:
                out.append(True)
            else:
                out.append(False)
        return out