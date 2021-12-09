#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        fail_jump = gen_next(searchWord)

        p_pos = 0
        cur_word = 1

        for s_pos, cur_char in enumerate(sentence):
            if cur_char == " ":
                cur_word += 1
                continue

            # 匹配的条件不仅是当前字符要匹配 还要从某单词开头匹配
            while p_pos != 0 and cur_char != searchWord[p_pos]:
                p_pos = fail_jump[p_pos - 1]

            if s_pos > p_pos and sentence[s_pos - p_pos - 1] != " ":
                continue

            if cur_char == searchWord[p_pos]:
                p_pos += 1
                
            if p_pos == len(searchWord):
                while p_pos > 0:
                    if sentence[s_pos] != " ":
                        p_pos -= 1
                    else:
                        cur_word -= 1
                    s_pos -= 1
                return cur_word
        
        return -1


def gen_next(tar_str):
    fail_jump = [0 for _ in range(len(tar_str))]

    prefix_cmp_ind = 0

    for suffix_cmp_ind in range(1, len(tar_str)):
        while prefix_cmp_ind != 0 and tar_str[suffix_cmp_ind] != tar_str[prefix_cmp_ind]:
            prefix_cmp_ind = fail_jump[prefix_cmp_ind - 1]
        
        if tar_str[suffix_cmp_ind] == tar_str[prefix_cmp_ind]:
            prefix_cmp_ind += 1
        
        fail_jump[suffix_cmp_ind] = prefix_cmp_ind 
    
    return fail_jump


# @lc code=end

