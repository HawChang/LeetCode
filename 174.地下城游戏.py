#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 利用动态规划求解
        # 但如果从左上到右下开始求解的话
        # 需要保留当前路径截止的生命值 以及当前路径要求的最小值
        # 且当一个格子有两条路径时 我们无法选择是剩余生命值大的好 还是生命值要求小的好
        # 简单来说就是 如此递归无法保证全局最优

        # 转换思路 对于剩余生命值 只要求大于1就行
        # 因此我们从右下终点出发 向左上反向动态规划
        # 各点的生命值要求 都能保证是当前能到终点的生命值要求
        # 因此dp[0][0]的值 就是能到达终点的 最小的生命值要求

        row = len(dungeon)
        if row == 0:
            return 1
        col = len(dungeon[0])
        if col == 0:
            return 1
        
        # 初始化动态矩阵
        min_table = [[None for _ in range(col + 1)] for _ in range(row + 1)]
        # 处理边界值

        # 对于最后一列和最后一行 都设为最大值
        for cur_row in range(row):
            min_table[cur_row][col] = float("inf")
        for cur_col in range(col):
            min_table[row][cur_col] = float("inf")
        
        # 只有终点的下方和右方的 设为1 保证迭代的逻辑正确
        min_table[row][col - 1] = 1
        min_table[row - 1][col] = 1
        
        for cur_row in range(row - 1, -1, -1):
            for cur_col in range(col - 1, -1, -1):
                cur_min = min(
                    min_table[cur_row + 1][cur_col],
                    min_table[cur_row][cur_col + 1],
                ) - dungeon[cur_row][cur_col]
                min_table[cur_row][cur_col] = max(cur_min, 1)
                
                #print("({},{}): {}".format(cur_row, cur_col, min_table))
        
        return min_table[0][0]

                    

# @lc code=end

