#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        # 前面加一个初始化的结果 即空字符时 解码数为1
        decode_num = [1] + [0] * len(s)

        for cur_index in range(len(s)):
            cur_decode_index = cur_index + 1
            cur_num = 0

            # 当前位能否作为单独一位
            if s[cur_index] != "0":
                cur_num += decode_num[cur_decode_index - 1]

            # 当前位与前一位组成编码
            # 从第二个字符开始考虑该情况
            if cur_index >= 1 and s[cur_index - 1] != "0":
                if 10 * int(s[cur_index - 1]) + int(s[cur_index]) <= 26:
                    cur_num += decode_num[cur_decode_index - 2]
            
            decode_num[cur_decode_index] = cur_num

        return decode_num[-1]
            
                
# @lc code=end

