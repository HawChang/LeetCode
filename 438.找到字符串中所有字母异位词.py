#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        total_diff = 0
        char_diff = [0 for _ in range(26)]

        def to_int(cur_char):
            return ord(cur_char) - ord('a')

        # 记录p
        for cur_char in p:
            char_diff[to_int(cur_char)] += 1
            total_diff += 1
        
        res_list = list()
        
        # 遍历s 更新diff
        for cur_ind, cur_char in enumerate(s):
            # 增加一个新的char
            cur_char_ord = to_int(cur_char)
            char_diff[cur_char_ord] -= 1
            if char_diff[cur_char_ord] < 0:
                total_diff += 1
            else:
                total_diff -= 1

            # 移除距当前char一个p长度之前的char
            if cur_ind >= p_len :
                prev_char_ord = to_int(s[cur_ind - p_len])
                char_diff[prev_char_ord] += 1
                if char_diff[prev_char_ord] > 0:
                    total_diff += 1
                else:
                    total_diff -= 1
            
            if total_diff == 0:
                res_list.append(cur_ind - p_len + 1)
        
        return res_list


# @lc code=end

