#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 笨比方法，适合我这种新手：先把链表转化为数组，然后利用Pop
        #函数删除掉目标点，然后把数组转化为列表，虽然这个方法用在这个题目
        #上并不贴切，但是涵盖的不少知识点
        if not head:
            return None
        benbi= []
        while head:
            benbi.append(head)
            head = head.next
        benbi.pop(-n)
        # 列表0,None，List 独行
        new = ListNode(None)
        d = new
        for i in range(len(benbi)):
            d.next = benbi[i]
            d = d.next
        d.next = None

        return new.next

# @lc code=end

