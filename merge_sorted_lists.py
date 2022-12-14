class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # Check if either of the lists is null
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # Choose head which is smaller of the two lists
        if l1.val < l2.val:
            temp = head = ListNode(l1.val)
            l1 = l1.next
        else:
            temp = head = ListNode(l2.val)
            l2 = l2.next
        # Loop until any of the list becomes null
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp.next = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        # Add all the nodes in l1, if remaining
        while l1 is not None:
            temp.next = ListNode(l1.val)
            l1 = l1.next
            temp = temp.next
        # Add all the nodes in l2, if remaining
        while l2 is not None:
            temp.next = ListNode(l2.val)
            l2 = l2.next
            temp = temp.next
        return head


s = Solution()
l3 = ListNode(4)
l2 = ListNode(2, l3)
l1 = ListNode(1, l2)
l6 = ListNode(4)
l5 = ListNode(3, l6)
l4 = ListNode(1, l5)
m = s.mergeTwoLists(l1, l4)
while m is not None:
    print(m.val)
    m = m.next