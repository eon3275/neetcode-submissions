# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None
        n1 = l1.val if l1 else 0
        n2 = l2.val if l2 else 0
        total = n1+n2+carry
        val = total%10
        carry = total//10
        l1_next = l1.next if l1 else None
        l2_next = l2.next if l2 else None
        return ListNode(val, self.addTwoNumbers(l1_next, l2_next, carry))