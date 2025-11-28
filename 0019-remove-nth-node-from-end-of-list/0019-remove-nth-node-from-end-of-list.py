class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node that points to head (helps when deleting the first node)
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # second is now just before the node to delete
        second.next = second.next.next

        # Return the new head
        return dummy.next
        