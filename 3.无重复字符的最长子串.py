#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #return self.lengthOfLongestSubstring1(s)
        return self.lengthOfLongestSubstring2(s)

    def lengthOfLongestSubstring2(self, s: str) -> int:
        s_len = len(s)
        char_set = set()

        max_len = 0
        left, right = 0, 0
        while right < s_len:
            while right < s_len and s[right] not in char_set:
                char_set.add(s[right])
                right += 1

            # 此时最长[left, right-1]
            if right - left > max_len:
                max_len = right - left

            # 如果rigth没有遍历到头
            # 则缩短left 准备下次右扩
            if right < s_len:
                while s[left] != s[right]:
                    char_set.remove(s[left])
                    left += 1
                char_set.remove(s[left])
                left += 1
        
        return max_len

    def lengthOfLongestSubstring1(self, s: str) -> int:
        char_ind_dict = dict()
        cur_start = -1
        max_len = 0

        for cur_ind, cur_char in enumerate(s):
            if cur_char in char_ind_dict and char_ind_dict[cur_char] > cur_start:
                cur_start = char_ind_dict[cur_char]
            else:
                # cur_start往后移的话 长度一定不是最长的 
                # 所以只在cur_start没变时 判断当前长度
                max_len = max(max_len, cur_ind - cur_start)
            char_ind_dict[cur_char] = cur_ind
        
        return max_len

# @lc code=end

