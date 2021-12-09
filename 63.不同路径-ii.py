#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        s = list()

        for row in range(len(obstacleGrid)):
            # 新的一行 加新的一行记录列表
            s.append([])
            for col in range(len(obstacleGrid[row])):
                # 计算s[row][col]的值
                cur_s = 0 
                # 若当前位置有障碍 则不需要算值 直接为0
                if obstacleGrid[row][col] != 1:
                    # 如果是初始位置 则为1
                    if row == 0 and col == 0:
                        cur_s = 1

                    # 否则计算该位置值
                    # 看上边的路
                    # 如果上边的路是障碍 则上边的路的数量为0 加上也没影响
                    if row != 0:
                        cur_s += s[row-1][col]

                    # 看左边的路
                    # 如果左边的路是障碍 则左边的路的数量为0 加上也没影响
                    if col != 0:
                        cur_s += s[row][col-1]

                #print("row = {}, col = {}, cur_s = {}".format(row, col, cur_s))
                s[row].append(cur_s)
        
        #print("s: {}".format(s))
        return s[-1][-1]


        
# @lc code=end

