#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return self.longestPalindrome1(s)
        # return self.longestPalindrome2(s)
        return self.longestPalindrome3(s)

    def longestPalindrome3(self, s: str) -> str:
        # dp[i]: 位置i的臂长。即以i为中心 能向左向右扩展多少个字符
        dp = list()

        max_arm = 0
        max_str = ""

        s = "#" + "#".join(s) + "#"

        cur_right = -1
        cur_center = -1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 到这里 上一次的匹配成功了 即[left + 1, right - 1]
            # 长度为l = ((right - 1) - (left + 1) + 1)
            # 该长度一定是奇数
            # 该字符串的臂长为(l - 1) // 2
            # 所以臂长为 (right - left - 2) // 2
            return (right - left - 2) // 2

        # 遍历s串各处
        for cur_ind in range(len(s)):
            # cur_ind在之前的回文串内 则可以少判断一些字符 从没开始判断的cur_right+1开始即可
            cur_arm = 0
            if cur_ind < cur_right:
                # 当前位置关于当前最右的回文子串的中心的对称点
                sym_ind = cur_center - (cur_ind - cur_center)

                # 对称位置已确认其臂长 又该臂长可能不完全在当前最右的回文子串中
                # 这里需要做判断
                sym_arm = dp[sym_ind]
                cover_length = cur_right - cur_ind

                # 这里可以分情况讨论
                # 当sym_arm cover_length不相等时 该处臂长就是较小的那个值
                # 当相等时，则需要继续判断
                if sym_arm < cover_length:
                    cur_arm = sym_arm
                elif sym_arm > cover_length:
                    cur_arm = cover_length
                else:
                    cur_arm = expand(cur_ind - sym_arm - 1, cur_ind + sym_arm + 1)

                # 将三种情况合起来的话 代码简单了点 但是会多余一些匹配操作
                # confirm_arm = min(sym_arm, cover_length)
                # cur_arm = expand(cur_ind - confirm_arm - 1, cur_ind + confirm_arm + 1)
            else:
                cur_arm = expand(cur_ind - 1, cur_ind + 1)
            
            dp.append(cur_arm)

            # 更新最右回文子串的记录
            if cur_arm + cur_ind > cur_right:
                cur_right = cur_arm + cur_ind
                cur_center = cur_ind
            
            # 更新最长回文的记录
            if cur_arm > max_arm:
                max_arm = cur_arm 
                max_str = s[cur_ind - cur_arm + 1: cur_ind + cur_arm + 1: 2]
        
        return max_str

    def longestPalindrome2(self, s: str) -> str:
        # 中心扩展法
        def central_expand(left, right):
            # 返回当前能扩展到的最长回文串
            if s[left] == s[right]:
                if (left == 0) or (right == (len(s) - 1)):
                    # 两侧到边界 停止扩展 最长为[left, right] 长度为right - left + 1
                    return s[left: right + 1]
                return central_expand(left - 1, right + 1)
            else:
                # 上一次为最长 为[left + 1, right - 1] 长度为right - 1 - left - 1 + 1
                return s[left + 1: right]
        
        s_size = len(s)
        max_len = 0
        max_str = ""

        def check_max(left, right):
            nonlocal max_len, max_str
            cur_str = central_expand(left, right)
            cur_len = len(cur_str)
            if cur_len > max_len:
                max_len = cur_len
                max_str = cur_str
        
        for cur_ind in range(s_size):
            check_max(cur_ind, cur_ind)
            if cur_ind + 1 < s_size:
                check_max(cur_ind, cur_ind + 1)
        
        return max_str

    def longestPalindrome1(self, s: str) -> str:
        s_size = len(s)
        # 状态转移方程 dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        dp = [[False for _ in range(s_size)] for _ in range(s_size)]
        # 特殊情况 dp[i][i] dp[i][i+1]

        max_length = 0
        max_str = ""

        for end_pos in range(s_size):
            for start_pos in range(end_pos + 1):
                if end_pos == start_pos:
                    dp[start_pos][end_pos] = True
                elif start_pos + 1 == end_pos:
                    dp[start_pos][end_pos] = True if s[start_pos] == s[end_pos] else False
                else:
                    dp[start_pos][end_pos] = dp[start_pos + 1][end_pos - 1] and s[start_pos] == s[end_pos]
                
                if dp[start_pos][end_pos]:
                    cur_length = end_pos - start_pos + 1
                    if max_length < cur_length:
                        max_length = cur_length
                        max_str = s[start_pos: end_pos + 1]
        
        return max_str


# @lc code=end

