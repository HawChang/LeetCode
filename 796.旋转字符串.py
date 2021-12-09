#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False

        fail_jump = gen_next(goal)
        cur_p_pos = 0

        for cur_char in s + s:
            while cur_p_pos != 0 and goal[cur_p_pos] != cur_char:
                cur_p_pos = fail_jump[cur_p_pos - 1]
            
            if goal[cur_p_pos] == cur_char:
                cur_p_pos += 1
            
            if cur_p_pos == len(goal):
                return True
            
        return False


def gen_next(s):
    fail_jump = [0 for _ in range(len(s))]
    p_cmp_ind = 0
    for s_cmp_ind in range(1, len(s)):
        while p_cmp_ind != 0 and s[p_cmp_ind] != s[s_cmp_ind]:
            p_cmp_ind = fail_jump[p_cmp_ind - 1]
        if s[p_cmp_ind] == s[s_cmp_ind]:
            p_cmp_ind += 1
        fail_jump[s_cmp_ind] = p_cmp_ind
    return fail_jump

# @lc code=end

