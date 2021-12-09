#
# @lc app=leetcode.cn id=1397 lang=python3
#
# [1397] 找到所有好字符串
#

# @lc code=start
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        return self.findGoodStrings_with_lru(n, s1, s2, evil)

    def findGoodStrings_with_lru(self, n, s1, s2, evil):
        # KMP
        fail_jump = gen_next(evil)
        # 回溯

        #count_record = dict()

        # 缓存输入对对应的输出结果
        # 也可以自己写count_record记录起来
        @lru_cache(None)
        def count(m_pos, p_pos, strict_small=True, strict_big=True):
            """ count(i, j) 字符串已确认前i个位置 已匹配到evil字符串第j个字符 该情况下符合要求的字符串数目
            """
            #print("m_pos = {}, p_pos = {}".format(m_pos, p_pos))
            # 如果m_pos已到n 说明已得到一个满足要求的字符串
            if m_pos == n:
                return 1
            
            # 否则继续往下计数

            # 满足要求的字符串总数
            total_count = 0

            cur_ord_min = ord(s1[m_pos]) if strict_small else ord("a")
            cur_ord_max = ord(s2[m_pos]) if strict_big else ord("z")

            # cur_char范围[cur_ord_min, cur_ord_max]
            for ord_val in range(cur_ord_min, cur_ord_max + 1):
                new_p_pos = p_pos

                if strict_small and ord_val == cur_ord_min:
                    new_strict_small = strict_small
                else:
                    new_strict_small = False

                if strict_big and ord_val == cur_ord_max:
                    new_strict_big = strict_big
                else:
                    new_strict_big = False

                # 当前要匹配的字符
                cur_char = chr(ord_val)
                # 
                while new_p_pos != 0 and evil[new_p_pos] != cur_char:
                    new_p_pos = fail_jump[new_p_pos - 1]

                if evil[new_p_pos] == cur_char:
                    new_p_pos += 1
                
                if new_p_pos == len(evil):
                    # 说明当前字符串已包含evil 剪枝
                    continue
                
                #key = "|".join([
                #    str(m_pos + 1),
                #    str(new_p_pos),
                #    str(new_strict_small),
                #    str(new_strict_big),
                #])

                #if key in count_record:
                #    cur_count = count_record[key]
                #else:
                #    cur_count = count(m_pos + 1, new_p_pos, new_strict_small, new_strict_big)
                #    count_record[key] = cur_count
                
                #total_count += cur_count
                total_count += count(m_pos + 1, new_p_pos, new_strict_small, new_strict_big)
            
            return total_count % int(1e9 + 7)
        
        # 字符串从0开始 匹配了0个字符
        return count(0, 0)


def gen_next(tar_str):
    fail_jump = [0 for _ in range(len(tar_str))]

    prefix_cmp_ind = 0

    for suffix_cmp_ind in range(1, len(tar_str)):
        while prefix_cmp_ind != 0 and tar_str[prefix_cmp_ind] != tar_str[suffix_cmp_ind]:
            prefix_cmp_ind = fail_jump[prefix_cmp_ind - 1]
        
        if tar_str[prefix_cmp_ind] == tar_str[suffix_cmp_ind]:
            prefix_cmp_ind += 1

        fail_jump[suffix_cmp_ind] = prefix_cmp_ind
    
    return fail_jump


# @lc code=end

