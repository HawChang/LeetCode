#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 遍历每层
        # 该层各高度可以由上一层得出
        # 每层根据直方图求最大矩形 单调栈即可计算

        row = len(matrix)
        col = len(matrix[0])

        # 前后各加一个高度为零的条
        heights = [0 for _ in range(col + 2)]

        max_area = 0

        # 遍历每一层
        for cur_row in range(row):

            # 根据当前层 更新heights
            for cur_col in range(col):
                if matrix[cur_row][cur_col] == '1':
                    heights[cur_col + 1] += 1
                else:
                    heights[cur_col + 1] = 0
            
            # 根据heights 计算当前层最大矩阵
            # 递增栈
            inc_stack = list()
            for cur_col, cur_height in enumerate(heights):
                while len(inc_stack) > 0 and inc_stack[-1][1] > cur_height:
                    _, mid_height = inc_stack.pop()
                    prev_ind = 0 if len(inc_stack) == 0 else inc_stack[-1][0] + 1
                    cur_area = (cur_col - prev_ind) * mid_height
                    if max_area < cur_area:
                        max_area = cur_area
                inc_stack.append((cur_col, cur_height))
        
        return max_area


# @lc code=end

