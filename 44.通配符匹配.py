#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_length = len(s)
        p_length = len(p)
        match_table = [[False for _ in range(s_length + 1)] for _ in range(p_length + 1)]

        match_table[0][0] = True
        for cur_p_ind, cur_p in enumerate(p):
            if cur_p == "*":
                # 看前一个
                match_table[cur_p_ind + 1][0] = match_table[cur_p_ind][0]
        
        for cur_p_ind, cur_p in enumerate(p):
            match_p_ind = cur_p_ind + 1
            for cur_s_ind, cur_s in enumerate(s):
                match_s_ind = cur_s_ind + 1
                if cur_p == "*":
                    match_table[match_p_ind][match_s_ind] |= \
                        match_table[match_p_ind][match_s_ind - 1] | \
                        match_table[match_p_ind - 1][match_s_ind]
                elif cur_p == "?" or cur_p == cur_s:
                    match_table[match_p_ind][match_s_ind] |= \
                        match_table[match_p_ind - 1][match_s_ind - 1]
        
        #print("match_table: {}".format(match_table)) 
        return match_table[p_length][s_length]


# @lc code=end

