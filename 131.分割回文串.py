#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 先动态规划 确认各子串是否回文串
        s_size = len(s)
        is_rev = [[None for j in range(s_size)] for i in range(s_size)]

        for r in range(s_size):
            for l in range(s_size):
                if l >= r:
                    is_rev[l][r] = True
                else:
                    # 因为l==s_size或r==0的情况都在l>=r中
                    # 所以这里不用检查了
                    is_rev[l][r] = is_rev[l + 1][r - 1] and (s[l] == s[r])

        #print("is_rev: {}".format(is_rev))
        
        # 根据各子串是否回文串来
        sub_lists = list()
        stack = list()
        stack.append((0, list()))
        while len(stack) > 0:
            cur_start, cur_list = stack.pop()
            if cur_start == s_size:
                sub_lists.append(cur_list)
                #print("append: {}".format(cur_list))
            for cur_end in range(cur_start, s_size):
                if is_rev[cur_start][cur_end]:
                    next_start = cur_end + 1
                    new_list = cur_list.copy()
                    new_list.append(s[cur_start:next_start])
                    stack.append((next_start, new_list))
        
        return sub_lists
        

# @lc code=end

