class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = list(range(-n//2,n//2+1))
        if n%2==0:
            out.remove(0)
            # return out
        else:
            # out = list(range(-n//2+1,n//2+1))
            del out[0]
        return out