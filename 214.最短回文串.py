#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""

        fail = [None for _ in range(length)]
        fail[0] = 0

        # 构造kmp的next数组
        for cur_ind in range(1, length):
            # 前一位的最长前缀长度 也就是本次初始的模式回退位置
            # 初始的模式回退位置 就是要判断是否相同的位置
            prev_ind = fail[cur_ind - 1]
            # 重复判断模式回退位置是否与当前位置相同
            # 直到无法回退
            while s[prev_ind] != s[cur_ind] and prev_ind > 0:
                # 当前位置与模式位置不同时 继续回退 
                # 回退位置是当前回退位置前一个位置对应的回退位置
                prev_ind = fail[prev_ind - 1]
            # 重复回退完成后 有可能是无法回退了 有可能是字符相同
            # 当字符相同时 当前位置的回退位置 在当前回退位置上+1
            if s[prev_ind] == s[cur_ind]:
                prev_ind += 1
            
            fail[cur_ind] = prev_ind
        
        print("fail: {}".format(fail))

        s_2 = s[::-1]
        cur_pattern_pos = 0
        for cur_pos in s_2:
            while cur_pattern_pos > 0 and cur_pos != s[cur_pattern_pos]:
                cur_pattern_pos = fail[cur_pattern_pos - 1]
            
            if cur_pos == s[cur_pattern_pos]:
                cur_pattern_pos += 1

            #print("cur_pattern_pos: {}".format(cur_pattern_pos))
        
        #print("fail: {}".format(fail))
        #print("cur_pattern_pos: {}".format())
        # kmp过完之后 cur_pattern_pos表示下一个要匹配的位置
        # 也是已匹配的字符串的长度
        # 则S1长度为cur_pattern_pos

        return  s[length - 1: cur_pattern_pos - 1: -1] + s


# @lc code=end

