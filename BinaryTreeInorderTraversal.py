# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inord = []
        def inorder(curr=root):
            nonlocal inord
            if curr:
                inorder(curr.left)
                inord.append(curr.val)
                inorder(curr.right)
            return
        inorder()
        return inord