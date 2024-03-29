# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return
        current = head
        while current.next!=None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head