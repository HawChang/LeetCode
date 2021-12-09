#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        visit = [[False for _ in range(col)] for _ in range(row)]

        def move(cur_row, cur_col):
            cur_pos = [cur_row, cur_col]
            for move_ind in range(len(cur_pos)):
                for move in [-1, 1]:
                    cur_pos[move_ind] += move
                    if 0 <= cur_pos[0] < row and \
                            0 <= cur_pos[1] < col and \
                            not visit[cur_pos[0]][cur_pos[1]]:
                        yield cur_pos
                    cur_pos[move_ind] -= move

        def search(cur_row, cur_col, cur_ind):
            #print("cur_row: {}, cur_col: {}, cur_ind: {}".format(cur_row, cur_col, cur_ind))
            if board[cur_row][cur_col] == word[cur_ind]:
                visit[cur_row][cur_col] = True
                if cur_ind == len(word) - 1:
                    return True

                for next_row, next_col in move(cur_row, cur_col):
                    if search(next_row, next_col, cur_ind + 1):
                        return True
                visit[cur_row][cur_col] = False
            
            return False
        
        for cur_row in range(row):
            for cur_col in range(col):
                if search(cur_row, cur_col, 0):
                    return True
        
        return False
        

                    




# @lc code=end

