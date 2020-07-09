#
# @lc app=leetcode.cn id=1480 lang=python3
#
# [1480] 一维数组的动态和
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]):
        '''
        sums = nums
        for i in range(1,len(nums)):
            sums[i] = sums[i-1]+nums[i]

        return sums'''
        sum = 0
        out=[]
        for i in range(len(nums)):
            sum += nums[i]
            out.append(sum)
        return out


# @lc code=end

