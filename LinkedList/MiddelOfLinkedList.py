# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        linkedList = []
        temp = head
        while head:
            linkedList.append(head)
            head = head.next
        return linkedList[len(linkedList)//2]