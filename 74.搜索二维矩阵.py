#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 当前复杂度O(M+N)
        # 用二分查找更快
        tar_row = None
        for cur_row_ind in reversed(range(len(matrix))):
            if matrix[cur_row_ind][0] <= target:
                tar_row = cur_row_ind
                break
        if tar_row is not None:
            for cur_elem in matrix[tar_row]:
                if cur_elem == target:
                    return True
                if cur_elem > target:
                    break
        return False
                
            
# @lc code=end

