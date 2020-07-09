#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode):
#       prev = None

        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr 
            curr = next
        return prev


# @lc code=end

