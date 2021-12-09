#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)
        dp = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]
        
        # dp[i][j]：word1到第i个字符 要编辑多少次 才能变成 word2到第j个字符
        # dp[0][i]：就是i 就是新增多少次
        # dp[i][0]：就是i 就是删除多少次
        for cur_ind in range(word1_len + 1):
            dp[cur_ind][0] = cur_ind
        for cur_ind in range(word2_len + 1):
            dp[0][cur_ind] = cur_ind

        for cur_word1_ind in range(1, word1_len + 1):
            for cur_word2_ind in range(1, word2_len + 1):
                # 如果此处两字符相等 则不需要替换 否则需要一次替换操作
                replace_op = 0 if word1[cur_word1_ind - 1] == word2[cur_word2_ind - 1] else 1
                dp[cur_word1_ind][cur_word2_ind] = min(
                    dp[cur_word1_ind][cur_word2_ind - 1] + 1,              # 删除当前word1字符
                    dp[cur_word1_ind - 1][cur_word2_ind] + 1,              # 增加当前word2字符
                    dp[cur_word1_ind - 1][cur_word2_ind - 1] + replace_op, # 替换（或保持原样）使两字符相等
                )
            
        return dp[word1_len][word2_len]


# @lc code=end

