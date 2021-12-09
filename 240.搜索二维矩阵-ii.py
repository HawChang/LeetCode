#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        cur_row = row - 1
        cur_col = 0
        while cur_row >= 0 and cur_col < col:
            if target > matrix[cur_row][cur_col]:
                cur_col += 1
            elif target < matrix[cur_row][cur_col]:
                cur_row -= 1
            else:
                return True
        return False

        
# @lc code=end

