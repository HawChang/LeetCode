#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching_v2(self, words: List[str]) -> List[str]:
        word_sort_by_length = sorted(words, key=lambda x:len(x), reverse=True)
        pattern_list = list()
        for pattern_ind in range(1, len(word_sort_by_length)):
            for match_ind in range(pattern_ind):
                if word_sort_by_length[pattern_ind] in word_sort_by_length[match_ind]:
                    pattern_list.append(word_sort_by_length[pattern_ind])
                    break

        return pattern_list

    def stringMatching(self, words: List[str]) -> List[str]:
        word_sort_by_length = sorted(words, key=lambda x:len(x), reverse=True)
        pattern_list = list()
        match_list = list()
        for cur_pattern in word_sort_by_length:
            succeed_flag = False
            for cur_match in match_list:
                if is_sub(cur_match, cur_pattern):
                    pattern_list.append(cur_pattern)
                    succeed_flag = True
                    break
            if not succeed_flag:
                match_list.append(cur_pattern)
        
        return pattern_list


def is_sub(s, p):
    fail_jump = gen_next(p)
    cur_p_pos = 0
    for cur_char in s:
        while cur_p_pos != 0 and p[cur_p_pos] != cur_char:
            cur_p_pos = fail_jump[cur_p_pos - 1]
        if p[cur_p_pos] == cur_char:
            cur_p_pos += 1
        if cur_p_pos == len(p):
            return True
    return False


def gen_next(s):
    fail_jump = [0 for _ in range(len(s))]
    p_cmp_ind = 0
    for s_cmp_ind in range(1, len(s)):
        while p_cmp_ind != 0 and s[s_cmp_ind] != s[p_cmp_ind]:
            p_cmp_ind = fail_jump[p_cmp_ind - 1]
        if s[s_cmp_ind] == s[p_cmp_ind]:
            p_cmp_ind += 1
        fail_jump[s_cmp_ind] = p_cmp_ind
    return fail_jump

# @lc code=end

