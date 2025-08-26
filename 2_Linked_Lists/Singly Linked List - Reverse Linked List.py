# difficulty: easy
# solution: https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150
# my solution

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        back = None
        temp = None
        while curr:
            temp = curr
            curr = curr.next
            temp.next = back
            back = temp

        return temp