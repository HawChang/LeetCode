#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        max_profit = None
        for cur_price in prices:
            if min_price is None or min_price > cur_price:
                min_price = cur_price
            
            cur_profit = cur_price - min_price
            if max_profit is None or cur_profit > max_profit:
                max_profit = cur_profit
        
        return max_profit


# @lc code=end

