#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(total_num, cur_num, cur_list):
            res_list = list()
            # 分三种情况
            # 1.不能加括号了 
            if total_num == n and cur_num == 0:
                res_list = cur_list

            # 2.加左括号
            if total_num < n:
                next_list = list()
                for cur_res in cur_list:
                    next_list.append(cur_res + '(')
                res_list.extend(gen(total_num + 1, cur_num + 1, next_list))

            # 3.加右括号
            if cur_num > 0:
                next_list = list()
                for cur_res in cur_list:
                    next_list.append(cur_res + ')')
                res_list.extend(gen(total_num, cur_num - 1, next_list))
            
            return res_list
        
        return gen(0, 0, [""])
            

# @lc code=end

