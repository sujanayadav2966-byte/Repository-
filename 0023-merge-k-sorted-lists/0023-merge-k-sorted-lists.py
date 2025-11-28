import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        heap = []
        # Initialize heap with the first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))  # (value, index, node)
        
        dummy = ListNode(0)
        current = dummy

        while heap:
            # Pop the smallest element
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            # If the node has a next, push it to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next