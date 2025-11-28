# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a linked list segment
        def reverse_segment(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # new head of reversed segment

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            # Find the k-th node
            kth = prev_group_end
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # Not enough nodes left

            next_group_start = kth.next

            # Reverse current k-group
            group_start = prev_group_end.next
            new_group_head = reverse_segment(group_start, next_group_start)

            # Connect previous part with the new head
            prev_group_end.next = new_group_head
            group_start.next = next_group_start

            # Move prev_group_end pointer
            prev_group_end = group_start
        