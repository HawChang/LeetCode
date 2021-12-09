#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        # 先动态规划 确认各子串是否回文串
        s_size = len(s)
        is_rev = [[None for j in range(s_size)] for i in range(s_size)]

        for r in range(s_size):
            for l in range(s_size):
                if l >= r:
                    is_rev[l][r] = True
                else:
                    # 因为l==s_size或r==0的情况都在l>=r中
                    # 所以这里不用检查了
                    is_rev[l][r] = is_rev[l + 1][r - 1] and (s[l] == s[r])

        #print("is_rev: {}".format(is_rev))
        
        # 根据各子串是否回文串来
        min_cut = [None for _ in range(s_size)]
        for cur_ind in range(s_size):
            # 需要判断 s[0:cur_ind]整体是否回文子串
            # 或者需要分割一次 s[j:cur_ind]为回文子串
            if is_rev[0][cur_ind]:
                min_cut[cur_ind] = 0
            else:
                for prev_cut_ind in range(cur_ind):
                    if is_rev[prev_cut_ind + 1][cur_ind]:
                        cur_cut_num = min_cut[prev_cut_ind] + 1
                        if min_cut[cur_ind] is None or min_cut[cur_ind] > cur_cut_num:
                            min_cut[cur_ind] = cur_cut_num

        return min_cut[s_size - 1]


# @lc code=end

