#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur_lists = [[]]
        for cur_num in nums:
            next_lists = list()
            for cur_list in cur_lists:
                next_lists.append(cur_list + [cur_num])
                next_lists.append(cur_list.copy())
            cur_lists = next_lists
        
        return cur_lists


# @lc code=end

