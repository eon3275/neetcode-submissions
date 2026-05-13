# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while curr and cnt<k:
            curr = curr.next
            cnt += 1
        if cnt==k:
            prev = None
            curr = head
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            if curr:
                head.next = self.reverseKGroup(curr, k)
            return prev
        return head