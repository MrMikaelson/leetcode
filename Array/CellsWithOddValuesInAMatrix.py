class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r = dict(zip(range(m),[0]*m))
        c = dict(zip(range(n),[0]*n))
        for i in indices:
            r[i[0]]+=1
            c[i[1]]+=1
        odd = 0
        for i in r:
            for j in c:
                if (r[i]+c[j])%2!=0:
                    odd += 1
        return odd