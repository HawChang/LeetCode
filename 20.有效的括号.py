#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        sym_dict = {
            ']': '[',
            '}': '{',
            ')': '(',
        }

        for cur_char in s:
            if cur_char in sym_dict:
                if len(stack) == 0:
                    return False
                top_char = stack.pop()
                if sym_dict[cur_char] != top_char:
                    return False
            else:
                stack.append(cur_char)
        
        return len(stack) == 0


# @lc code=end

