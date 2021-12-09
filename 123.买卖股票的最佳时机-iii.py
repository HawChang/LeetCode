#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 记录五种状态
        # 0. 无操作
        # 1. 买入一次
        # 2. 交易一次
        # 3. 买入两次
        # 4. 交易两次 

        days = len(prices)
        p_table = [[None for _ in range(days)] for _ in range(5)]

        for i in range(days):
            p_table[0][i] = 0
        
        p_table[1][0] = p_table[0][0] - prices[0] 
        p_table[2][0] = p_table[1][0] + prices[0]
        p_table[3][0] = p_table[2][0] - prices[0]
        p_table[4][0] = p_table[3][0] + prices[0]

        for cur_day, cur_price in enumerate(prices):
            # 无操作 table无任何变化
            # 买入一次
            # 以前买入和今天买入的最大值
            if cur_day == 0:
                continue

            p_table[1][cur_day] = max(
                p_table[1][cur_day - 1],
                p_table[0][cur_day] - cur_price,
                )
            # 交易一次
            # 以前完成交易的最大值 和今天完成交易的最大值
            # 这里可以当天买入 当天卖出
            p_table[2][cur_day] = max(
                p_table[2][cur_day - 1],
                p_table[1][cur_day] + cur_price,
            )
            # 买入两次
            p_table[3][cur_day] = max(
                p_table[3][cur_day - 1],
                p_table[2][cur_day] - cur_price,
            )
            # 交易两次
            p_table[4][cur_day] = max(
                p_table[4][cur_day - 1],
                p_table[3][cur_day] + cur_price,
            )
        
        print(p_table)
        return p_table[4][days - 1]

        
# @lc code=end

