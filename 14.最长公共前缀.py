#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_pre = ""

        min_len = min([len(s) for s in strs])
        for cur_ind in range(min_len):
            cur_char = None
            for cur_str in strs:
                if cur_char is None:
                    cur_char = cur_str[cur_ind]
                elif cur_char != cur_str[cur_ind]:
                    return common_pre
            
            if cur_char is not None:
                common_pre += cur_char

        return common_pre

                
# @lc code=end

