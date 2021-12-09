#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """计数
        """
        max_length = 0
        def count_pair(l, left_char, right_char):
            nonlocal max_length
            left_count = 0
            right_count = 0

            # 从左往右遍历 统计左右括号的数目
            for cur_char in l: 
                if cur_char == left_char:
                    left_count += 1
                else:
                    right_count += 1
                
                if right_count > left_count:
                    # 当右侧字符大于左侧字符时 清空统计值
                    # 因为之后的字符串影响不了之前的情况
                    left_count = 0
                    right_count = 0
                elif right_count == left_count:
                    # 当左侧字符数等于右侧字符数时
                    # 我们可以保证当前统计范围里，任意包含开头的子字符串都满足左括号大于右括号
                    # 且当前范围里左括号等于右括号
                    # 因此此时就是最长的有效括号
                    cur_max_length = left_count * 2
                    if cur_max_length > max_length:
                        max_length = cur_max_length
                
                # 当左侧字符数大于右侧时
                # 该类情况无法判断有效括号长度
                # 例如"(()(()"中左括号4 右括号2 但有效括号长度并不是4
                # 此类情况一次遍历无法解决 只能再反向遍历一遍解决

        # 正反遍历 覆盖所有情况
        count_pair(s, "(", ")")
        count_pair(s[::-1], ")", "(")

        return max_length

    def longestValidParentheses2(self, s: str) -> int:
        """利用栈
        """
        stack = list()
        # 这里放最后一个没有被匹配的右括号的ind值
        stack.append(-1)

        max_length = 0
        for cur_ind, cur_s in enumerate(s): 
            if cur_s == ")":
                stack.pop()
                # 如果此时stack为空 说明当前弹出的是最后一个右括号了
                if len(stack) == 0:
                    stack.append(cur_ind)
                else:
                    prev_left = stack[-1]
                    cur_max_length = cur_ind - prev_left
                    if max_length < cur_max_length:
                        max_length = cur_max_length
            else:
                stack.append(cur_ind)
            #print("cur_ind: {}, cur_stack: {}".format(cur_ind, stack))
        
        prev_left = stack.pop()
        cur_max_length = len(s) - prev_left - 1
        if max_length < cur_max_length:
            max_length = cur_max_length

        return max_length


# @lc code=end

