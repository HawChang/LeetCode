#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        return self.decodeString1(s)

    def decodeString1(self, s: str) -> str:
        if len(s) == 0:
            return ""

        ord_a = ord('a')
        ord_z = ord('z')
        ord_0 = ord('0')
        ord_9 = ord('9')

        # 示例abc2[aabc26[bc]aaa]cba6[bc]b
        # 将其看作是1[]内的字符串 
        # decode(abc2[aabc26[bc]aaa]cba6[bc]b) = abc+2*decode(aabc+26*decode(bc)+aaa)+cba+6*decode(bc)+b

        def decode(cur_ind=0):
            # 分情况
            # 起始是数字 还是 字母
            res = ""
            while cur_ind < len(s) and s[cur_ind] != "]":
                cur_ord = ord(s[cur_ind])
                # 如果遇到数字
                if ord_0 <= cur_ord <= ord_9:
                    # 解析出数值
                    repeat_num = 0
                    while cur_ind < len(s) and s[cur_ind] != "[":
                        repeat_num = repeat_num * 10 + ord(s[cur_ind]) - ord_0
                        cur_ind += 1
                    # 跳过[ 解析[]内的字符串情况 遇到对应的]就退出了
                    # 因为在[]内部如果还有[] 其会被递归调用 所以其遇不到别的] 越到的]就是对应的]
                    decode_res, decode_end_ind = decode(cur_ind + 1)
                    # 结果 += 重复次数 * []内的字符串
                    res += decode_res * repeat_num
                    # 跳过]
                    cur_ind = decode_end_ind + 1
                else:
                    res += s[cur_ind]
                    cur_ind += 1
            return res, cur_ind
        
        return decode()[0]
            

# @lc code=end