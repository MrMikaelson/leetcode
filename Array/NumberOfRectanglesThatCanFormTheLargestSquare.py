class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        side = [min(i) for i in rectangles]
        return side.count(max(side))