#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 对于数i 去除其最高位的1 得到另一个数j dp[i] = dp[j] + 1
        # 例如7（0111）去除最高位的1之后为3（0011），dp[7] = dp[3] + 1
        # 我们要遍历1到n 就要随时记录当前最高位的1 对应的数是多少
        # 设该数为k 则dp[i] = dp[j - k] + 1
        dp = [0 for _ in range(n + 1)]
        k = 1
        for cur_n in range(1, n + 1):
            # 当 cur_n是k的两倍时 说明 cur_n是2的整数次幂 更新最高位的对应值k
            if k * 2 == cur_n:
                k = cur_n

            dp[cur_n] = dp[cur_n - k] + 1
        
        return dp

# @lc code=end

