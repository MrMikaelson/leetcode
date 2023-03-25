class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heightDictionary = dict(zip(heights,names))
        heights.sort(reverse=True)
        return [heightDictionary[i] for i in heights]