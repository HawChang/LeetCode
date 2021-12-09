#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:

        def go_through(rate_list):
            value_list = list()
            cur_value = 1
            prev_rate = None
            for cur_rate in rate_list:
                if prev_rate is not None and prev_rate < cur_rate:
                    cur_value += 1
                else:
                    cur_value = 1
                
                prev_rate = cur_rate
                value_list.append(cur_value)
            return value_list
        
        value_list_1 = go_through(ratings)
        value_list_2 = go_through(ratings[::-1])[::-1]
        total_value = 0
        for value_1, value_2 in zip(value_list_1, value_list_2):
            total_value += max(value_1, value_2)
        
        return total_value


# @lc code=end

