#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combine_res_list = list()

        candidates_len = len(candidates)
        # stask[i] = (combine_list, start_index, cur_sum)
        stack = list()
        stack.append((list(), 0, 0))
        while len(stack) > 0:
            cur_list, cur_start_index, cur_sum = stack.pop()
            for cur_candidate_index in range(cur_start_index, candidates_len):
                cur_candidate = candidates[cur_candidate_index]
                new_sum = cur_sum + cur_candidate
                if new_sum < target:
                    stack.append((
                        cur_list + [cur_candidate],
                        cur_candidate_index,
                        new_sum,

                    ))
                elif new_sum == target:
                    combine_res_list.append(cur_list + [cur_candidate])
        return combine_res_list



# @lc code=end

