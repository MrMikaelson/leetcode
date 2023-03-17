class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for i in sentences:
            if len(i.split(" ")) > maximum:
                maximum = len(i.split(" "))
        return maximum