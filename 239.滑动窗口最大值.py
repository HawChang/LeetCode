#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res_list = list()
        # 单调递减栈
        dec_stack = list()

        for cur_ind, cur_num in enumerate(nums):
            # 去除栈里超过窗口的元素
            while len(dec_stack) > 0 and dec_stack[0][0] <= cur_ind - k:
                dec_stack.pop(0)
            
            # 尝试将当前值加入单调递减栈
            # 将栈里小于等于该值的都弹出
            while len(dec_stack) > 0 and dec_stack[-1][1] <= cur_num:
                dec_stack.pop()
            
            dec_stack.append((cur_ind, cur_num))
            
            if cur_ind >= k - 1:
                # 从k-1开始
                # 添加当前最大值
                res_list.append(dec_stack[0][1])
        
        return res_list


# @lc code=end

