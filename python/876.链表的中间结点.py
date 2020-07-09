# @before-stub-for-debug-begin
from python3problem876 import *
from typing import *
# @before-stub-for-debug-end

    #
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 111111 和之前一样的笨比方法，先把链表转化为数组，然后用数组来实现，这道题比找到倒数第几个点简单一点是由于
        #不需要再把数组转化为列表
        '''
        benbi=[]
        while head:
            benbi.append(head)
            head = head.next
            # % 取余，//取整
            #这个输出的为什么是列表啊，列表不是点点吗
        out = benbi[len(benbi)//2]
        return out
        '''
        #  22222 快满指针方法，快指针一次走两步，慢指针一次走一步，这样当快指针走完的时候，慢指针
        #刚好走到终点，
        '''
        slow = head
        fast = head
        # 这里的fast很重要，因为最后一步可能会溢出（当fast为空时没有next属性，此时却还要往前走，肯定错误）
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 
        '''
        ###法3，遍历（注意和法1 对比）
        if not head:
            return None
        num = 0 
        node = head
        while node:
            node  = node.next
            num+=1
        count = num//2
        while count!=0:
            count-=1
            head = head.next

        return head
        



        
# @lc code=end

