#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_length = len(s)
        p_length = len(p)
        match_table = [[False for i in range(s_length + 1)] for j in range(p_length + 1)]

        # 初始化dp矩阵
        # dp[0][0]为True
        match_table[0][0] = True

        # 对于dp[i][0]
        # 如果p的第i个字符，即[i-1]，为"*"，则有可能匹配时第i-1个字符和第i个字符都会被省略
        # 因此dp[i][0]为False和dp[i-2][0]的逻辑或
        for i, cur_p in enumerate(p):
            if cur_p == "*":
                match_table[i + 1][0] |= match_table[i - 1][0]
        
        def matches(cur_p, cur_s):
            if cur_p == "." or cur_p == cur_s:
                return True
            return False

        for cur_s_ind, cur_s in enumerate(s):
            # match_dp中当前s位置
            match_s_ind = cur_s_ind + 1
            for cur_p_ind, cur_p in enumerate(p):
                # match_dp中当前p位置
                match_p_ind = cur_p_ind + 1
                # 如果p[i]为* 
                # 若p[i-1]和s[j]匹配，则m[i][j]=m[i][j-1] or m[i-2][j]
                # 若p[i-1]和s[j]不匹配，则m[i][j]=m[i-2][j]
                # 所以不论如何 该值都受m[i-2][j]的影响
                # 如果匹配，还受m[i][j-1]的影响
                if cur_p == "*":
                    #if cur_s_ind == 0:
                    #    continue
                    assert cur_p_ind > 0
                    prev_p = p[cur_p_ind - 1]
                    assert prev_p != "*"
                    match_table[match_p_ind][match_s_ind] |= match_table[match_p_ind - 2][match_s_ind]
                    if matches(p[cur_p_ind - 1], cur_s):
                        match_table[match_p_ind][match_s_ind] |= match_table[match_p_ind][match_s_ind - 1]
                elif matches(cur_p, cur_s):
                    # 如果p[i]不为* 则一定匹配一个字符
                    match_table[match_p_ind][match_s_ind] = match_table[match_p_ind - 1][match_s_ind - 1]
        
        print("match_table: {}".format(match_table))
        return match_table[p_length][s_length]

        
# @lc code=end

