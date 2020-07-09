#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        定义一个快指针和慢指针,每次快指针走2步，慢指针走1步，判断快指针是否与慢指针重逢
        if head==None or head.next==None:
            return False
        
        slow = head
        fast = slow.next
        while(slow != fast):
            if (fast==None or fast.next==None):
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        '''
        try:
            slow = head
            fast = head.next
            while(slow != fast):
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
        
# @lc code=end

