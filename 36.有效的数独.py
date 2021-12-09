#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = [[0 for _ in range(9)] for _ in range(9)]
        col_count = [[0 for _ in range(9)] for _ in range(9)]
        square_count = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]

        for cur_row in range(9):
            for cur_col in range(9):
                cur_char = board[cur_row][cur_col]
                if cur_char == '.':
                    continue

                # num范围[1,9] 所以这里要减1
                cur_num = ord(cur_char) - ord('0') - 1
                row_count[cur_row][cur_num] += 1
                if row_count[cur_row][cur_num] > 1:
                    return False
                col_count[cur_col][cur_num] += 1
                if col_count[cur_col][cur_num] > 1:
                    return False
                square_count[cur_row // 3][cur_col // 3][cur_num] += 1
                if square_count[cur_row // 3][cur_col // 3][cur_num] > 1:
                    return False
        return True



# @lc code=end

