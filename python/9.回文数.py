#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        ''' 纯数学方法一
        if x < 0:
            return False
        num,total = x,0
        while num > 0:
            total = total*10 + num%10
            num = num//10

        if total == x:
            return True
        else:
            return False'''
        ### 解法二：转化为字符串
        '''
        return str(x)==str(x)[::-1]
        '''
        if x<0 or (x%10==0 and x!=0):
            return False
        num = 0
        while x>num:
            num = num*10 + x%10
            x//=10
        return x==num or num//10==x

# @lc code=end

