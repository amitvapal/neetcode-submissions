# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        
        #finding the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the list into two
        first = head
        second = slow.next
        slow.next = None
        
        prev, curr = None, second
        # reversing the linkedlist
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr=nxt

        #merging the twolists
        while first and prev:
            tmp1 = first.next
            tmp2 = prev.next

            first.next = prev
            prev.next = tmp1

            first = tmp1
            prev = tmp2

        return None
            
            





        