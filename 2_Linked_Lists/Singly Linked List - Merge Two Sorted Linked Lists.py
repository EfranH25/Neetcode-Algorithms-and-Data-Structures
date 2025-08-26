# difficulty: easy
# solution: https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode150
# my solution

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    # NOTE: mine is more complicated because I though I was modifying the existing lists into a 1 list. For the solution, you could start with empty list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2

        if p1 is None:
            return p2
        elif p2 is None:
            return p1

        if p1.val < p2.val:
            curr = p1
            p1 = p1.next
        else:
            curr = p2
            p2 = p2.next

        start = curr

        while curr:
            if p1 is None:
                curr.next = p2
                break
            elif p2 is None:
                curr.next = p1
                break


            if p1.val <= p2.val:
                curr.next = p1
                curr = p1
                p1 = p1.next
            else:
                curr.next = p2
                curr = p2
                p2 = p2.next

        return start

class SolutionAnswer:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next