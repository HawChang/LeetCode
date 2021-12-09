#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        self.small_min = ord("a")
        self.small_max = ord("z")
        res_list = list()
        for cur_query in queries:
            res = self.canMatch_once(cur_query, pattern)
            res_list.append(res)
        
        return res_list
    
    def canMatch(self, query, pattern):
        """分段匹配
        """
        cur_q_start= None 
        cur_p_start = None

        cur_q_end = 0
        cur_p_end = 0

        def get_next_end(tar_str, cur_end):
            if cur_end == len(tar_str):
                return None

            next_end = cur_end + 1
            while next_end < len(tar_str) and self.small_min <= ord(tar_str[next_end]) <= self.small_max:
                next_end += 1
            return next_end
        
        # 初始化 找到两字符串各自的第一个大写字母
        cur_q_end = get_next_end(query, -1)
        cur_p_end = get_next_end(pattern, -1)

        while cur_q_end < len(query) and cur_p_end < len(pattern):
            cur_q_start = cur_q_end
            cur_p_start = cur_p_end
            cur_q_end = get_next_end(query, cur_q_end)
            cur_p_end = get_next_end(pattern, cur_p_end)

            if query[cur_q_start] != pattern[cur_p_start]:
                return False
            
            # 这里不需要连续 所以不用KMP
            cur_p_pos = cur_p_start + 1
            cur_q_pos = cur_q_start + 1
            while cur_p_pos < cur_p_end and cur_q_pos < cur_q_end:
                if query[cur_q_pos] == pattern[cur_p_pos]:
                    cur_p_pos += 1
                
                cur_q_pos += 1
            
            if cur_p_pos != cur_p_end:
                return False
            
        if cur_q_end != len(query) or cur_p_end != len(pattern):
            return False
        
        return True
    
    def canMatch_once(self, query, pattern):
        """一遍匹配
        """
        cur_q_pos = 0
        cur_p_pos = 0

        while cur_q_pos < len(query) and cur_p_pos < len(pattern):
            cur_q_char = query[cur_q_pos]
            cur_p_char = pattern[cur_p_pos]
            # 匹配时 则准备匹配下一个pattern
            if cur_p_char == cur_q_char:
                cur_p_pos += 1
            elif not self.small_min <= ord(cur_q_char) <= self.small_max:
                # 没匹配时 如果query是大写 则失败
                return False

            cur_q_pos += 1
        
        # 若pattern未匹配完 则失败
        if cur_p_pos != len(pattern):
            return False
        
        # 若未匹配的qury里还有大写字母 则失败
        for cur_q_char in query[cur_q_pos:]:
            if not self.small_min <= ord(cur_q_char) <= self.small_max:
                return False
        
        return True


# @lc code=end

