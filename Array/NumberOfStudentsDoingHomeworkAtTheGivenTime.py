class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        out = 0
        for t in range(len(startTime)):
            if startTime[t] <= queryTime and queryTime <= endTime[t]:
                out += 1
        return out