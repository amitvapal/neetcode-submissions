# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # figure out half of list
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        #split half of list and revers that halp of list
        second = slow.next
        first = head
        slow.next = None

        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #merge both parts of list
        second = prev

        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
        return