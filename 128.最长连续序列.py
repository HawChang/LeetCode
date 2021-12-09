#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for cur_num in num_set:
            # 有前驱 则cur_num起手的一定不是最长的
            if cur_num - 1 in num_set:
                continue
            check_num = cur_num + 1
            cur_len = 1
            while check_num in num_set:
                cur_len += 1
                check_num += 1
            if cur_len > res:
                res = cur_len
        return res


# @lc code=end

