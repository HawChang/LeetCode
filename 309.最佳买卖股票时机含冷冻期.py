#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """空间可以优化至O(1)
        """
        day_num = len(prices)
        if day_num == 0:
            return 0

        no_op = [0 for _ in range(day_num)]
        buy   = [0 for _ in range(day_num)]
        sell  = [0 for _ in range(day_num)]

        buy[0] = -prices[0]

        for cur_ind in range(1, day_num):
            no_op[cur_ind] = max(
                no_op[cur_ind - 1],
                sell[cur_ind - 1],
                )

            buy[cur_ind] = max(
                buy[cur_ind - 1],
                no_op[cur_ind - 1] - prices[cur_ind],
            )

            sell[cur_ind] = buy[cur_ind - 1] + prices[cur_ind]
        
        return max(sell[day_num - 1], no_op[day_num - 1])


# @lc code=end

