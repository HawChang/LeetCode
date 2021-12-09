#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return self.permute1(nums)
        return self.permute2(nums)

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = list()
        def gen(rand_ind):
            if len(nums) == rand_ind:
                res.append(nums.copy())

            for cur_ind in range(rand_ind, len(nums)):
                nums[cur_ind], nums[rand_ind] = nums[rand_ind], nums[cur_ind]
                gen(rand_ind + 1)
                nums[cur_ind], nums[rand_ind] = nums[rand_ind], nums[cur_ind]
            
        gen(0)
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = list()
        def gen(cur_list, rest_nums):
            if len(rest_nums) == 0:
                res.append(cur_list.copy())

            for cur_ind, cur_num in enumerate(rest_nums):
                new_rest_nums = rest_nums[:cur_ind] + rest_nums[cur_ind+1:]
                cur_list.append(cur_num)
                gen(cur_list, new_rest_nums)
                cur_list.pop()
            
        gen([], nums)
        return res

# @lc code=end

