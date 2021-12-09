#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_char_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        if len(digits) == 0:
            return []
        
        def gen(cur_ind, cur_list):
            if cur_ind == len(digits):
                return cur_list
            next_list = list()
            for cur_char in number_char_dict[digits[cur_ind]]:
                for cur_str in cur_list:
                    next_list.append(cur_str + cur_char)
            return gen(cur_ind + 1, next_list)
        
        return gen(0, [""])



# @lc code=end

