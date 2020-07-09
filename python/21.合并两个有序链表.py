#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#### 递归 不明白
     
        if  not l1: return l2  # 终止条件，直到两个链表都空
        if  l2==None: return l1
        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        '''
        while not l1 or  not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1,l2.next)
            return l2
            '''

@lc code=end

