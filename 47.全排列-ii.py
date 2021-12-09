#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        path = list()
        def dfs(path, used):
            # 如果路径长度等于列表长
            # 则返回结果
            if len(path) == len(nums):
                return [path.copy()]
            cur_res_list = list()
            cur_used_set = set()
            # 遍历每个点
            # 忽略已用了的点和本次已遍历了的点
            for index, cur_num in enumerate(nums):
                if used[index]:
                    continue
                if cur_num in cur_used_set:
                    continue
                cur_used_set.add(cur_num)

                # 标记
                used[index] = True
                path.append(cur_num)
                cur_res_list.extend(dfs(path, used))
                # 取消标记
                used[index] = False
                path.pop()
            return cur_res_list

        res_list = dfs(path, used)
        return res_list
                

# @lc code=end

