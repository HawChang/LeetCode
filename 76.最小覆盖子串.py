#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = collections.defaultdict(int)
        w_dict = collections.defaultdict(int)

        for cur_char in t:
            t_dict[cur_char] += 1

        left_p, right_p = 0, 0
        sub_s = ""
        min_length = None

        def check():
            for cur_char, tar_count in t_dict.items():
                if tar_count > w_dict[cur_char]:
                    return False
            return True

        # right_p不包含 所以范围在[0, len(s)]
        while left_p < len(s) and right_p <= len(s):
            #print("left_p: {}, right: {}".format(left_p, right_p))
            if check():
                cur_length = right_p - left_p
                if min_length is None or min_length > cur_length:
                    min_length = cur_length
                    sub_s = s[left_p:right_p]
                w_dict[s[left_p]] -= 1
                left_p += 1
            else:
                # 当check失败 且right_p为len(s)时 说明结束 
                if right_p == len(s):
                    break
                w_dict[s[right_p]] += 1
                right_p += 1
        
        return sub_s

# @lc code=end

