#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 添加两辅助值更好地处理边界问题
        heights = [0] + heights + [0]

        height_stack = list()
        max_area = 0
        for cur_ind, cur_height in enumerate(heights):
            while len(height_stack) > 0:
                _, prev_height = height_stack[-1]
                if prev_height <= cur_height:
                    break

                # 如果当前柱高度小于栈顶柱高度
                # 则栈顶柱的面积就能确定了
                # 高即栈顶柱的高 宽为栈顶柱的前一个柱到当前柱的距离
                height_stack.pop()
                # 栈顶柱左右两边柱子的位置 决定矩形的宽
                # 这里取的是原栈顶柱的前一个柱的位置
                prev_ind, _ = height_stack[-1]

                prev_max_area = prev_height * (cur_ind - prev_ind - 1)
                if max_area < prev_max_area:
                    max_area = prev_max_area
            
            height_stack.append((cur_ind, cur_height))
        
        return max_area

            
# @lc code=end

