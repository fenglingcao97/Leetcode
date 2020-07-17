#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        #笨比方法
        '''
        dt = {'(': ')', '{': '}', '[': ']'}
        l = []
        if len(s) == 0:
            return True
        for i in range(len(s)):
            if not l:
                l.append(s[i])
                continue
            #
            #l=['(']
            #l[-1]=(
            if l[-1] in dt:
                # dt[l[-1]] = )
                if dt[l[-1]] == s[i]:
                    l.pop(-1)
                else:
                    l.append(s[i])
            else:
                return False
        if not l:
            return True
        return False
        '''
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False 
        return len(stack) == 1

# @lc code=end

