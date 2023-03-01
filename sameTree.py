# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p!=None and q!=None:
            print(p.val,q.val)
            if p.val == q.val:
                if not self.isSameTree(p.left,q.left):
                    return False
                if not self.isSameTree(p.right,q.right):
                    return False
            else:
                return False
        elif (p==None and q!=None) or (p!=None and q==None):
            print("Bro")
            return False
        return True