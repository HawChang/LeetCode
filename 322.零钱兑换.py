#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChange1(coins, amount)
        #return self.coinChange2(coins, amount)

    def coinChange1(self, coins: List[int], amount: int) -> int:
        """对于当前coin c: dp[amount] = 1 + dp[amount - c]
        """
        dp = [0 for _ in range(amount + 1)]
        for cur_num in range(1, amount + 1):
            min_coin_num = None
            for cur_coin in coins:
                cur_rest = cur_num - cur_coin
                if cur_rest >= 0 \
                        and dp[cur_rest] is not None \
                        and (min_coin_num is None or min_coin_num > dp[cur_rest]):
                    min_coin_num = dp[cur_rest]
            if min_coin_num is not None:
                min_coin_num += 1
            dp[cur_num] = min_coin_num
        
        return -1 if dp[amount] is None else dp[amount]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """回溯法会超时
        """
        sort_coins = sorted(coins, reverse=True)
        #print("sort: {}".format(sort_coins))
        total_min_num = None
        def check(cur_ind, tar_amount, cur_num=0):
            nonlocal total_min_num

            #print("cur_ind: {}, tar_amount: {}, cur_num: {}".format(cur_ind, tar_amount, cur_num))
            # 在cur_ind有两种选择 用该处硬币 和不用
            # 用了之后的情况 再下一个check检测
            # 所以结束条件有两种情况
            # 1. tar_amount为0 说明上一个cur_ind就完成了
            # 2. cur_ind == len(conins) 说明此时tar_amount不为0 且此时已遍历完数组 说明当前方案失败

            if tar_amount == 0:
                total_min_num = cur_num
                return

            # tar_amount小于0 或 数组遍历完 说明方案失败            
            if cur_ind == len(coins) or tar_amount < 0:
                return
            
            if total_min_num is None or cur_num < total_min_num - 1:
                check(cur_ind, tar_amount - sort_coins[cur_ind], cur_num + 1)
                check(cur_ind + 1, tar_amount, cur_num)
        
        check(0, amount)
        return -1 if total_min_num is None else total_min_num


# @lc code=end

