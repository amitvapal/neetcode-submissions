import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #intialzie heap
        min_heap = []

        #fill heap with list head values consisting of head_node.val, i, head_node
        for i, head_node in enumerate(lists):
            if head_node:
                heapq.heappush(min_heap, (head_node.val, i, head_node))
        #made dummy node
        dummy_node = ListNode(-1)
        current_pointer = dummy_node

        #loop through min heap traverse accordingly
        while min_heap:
            val, list_idx, node_to_add = heapq.heappop(min_heap)
            current_pointer.next = node_to_add
            current_pointer = current_pointer.next

            if node_to_add.next:
                heapq.heappush(min_heap, (node_to_add.next.val,list_idx, node_to_add.next))

        return dummy_node.next