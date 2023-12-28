# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Link:https://leetcode.com/problems/reverse-linked-list/
 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # this Solution in O(N) time complexity and O(1) space complexity
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    
    def reverseListrecursive(self, head: Optional[ListNode]) -> Optional[ListNode]: #this solution in O(N) time complexity and O(N) space complexity
        preHead = ListNode(-1)
        while head:
            tempNode = ListNode(head.val)
            tempNode.next = preHead.next
            preHead.next = tempNode
            head = head.next
        return preHead.next