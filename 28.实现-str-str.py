#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 生成next数组
        fail_jump = gen_next(needle)
        # 匹配串和模式串指针均初始为0
        s_pos = 0
        p_pos = 0

        # 一直找 
        # 直到p_pos到达needle的长度
        # 或者s_pos达到haystack的长度
        while p_pos < len(needle) and s_pos < len(haystack):
            # 如果当前位置字符不匹配 
            # 则模式串根据fail_jump的指示回退
            # 直到回退到能匹配的位置 或者 不能回退的时候
            while p_pos != 0 and needle[p_pos] != haystack[s_pos]:
                # 回退的位置 = fail_jump中 本次匹配的模式串位置的前一个位置 的值
                p_pos = fail_jump[p_pos - 1]
            
            if needle[p_pos] == haystack[s_pos]:
                p_pos += 1
            
            s_pos += 1
        
        if p_pos < len(needle):
            return -1
        else:
            return s_pos - p_pos


    def strStr2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        # 拼接字符串为needle#haystack
        # 因为#是特殊字符 不会存在于needle和haystack中
        # 则当fail_jump中 某处值为len(needle)时
        # 说明needle变成了公共前后缀
        # 也即hay_stack中出现了needle
        fail_jump = gen_next("{}#{}".format(needle, haystack))
        # 这里其实没必要算出needle#haystack全部的fail_jump数组
        # 只要出现了len(needle)就能结束
        # 这里为了直接调用gen_next 所以这么写
        for cur_offset in range(len(haystack)):
            cur_ind = cur_offset + len(needle) + 1
            if fail_jump[cur_ind] == len(needle):
                return cur_offset - len(needle) + 1
        return -1

    
def gen_next(tar_str):
    # 当位置i匹配失败后
    # fail_jump[i] = j: 此时是尝试匹配模式串i+1处字符，匹配失败后，找已匹配成功的最后一个字符 也就是i处的字符
    # 对应的位置j，该位置的意思是，已经匹配到了i处，接下来匹配要匹配i+1处字符的位置
    # 也就是说 当模式串i+1处的位置匹配失败后 模式串指针跳到fail_jump[i-1] 该处继续匹配当前匹配串位置
    fail_jump = [0 for _ in range(len(tar_str))]
    # 当前后缀准备匹配前缀的位置
    prefix_cmp_ind = 0
    # 字符串从第二个字符开始，依次遍历 作为当前后缀要匹配的位置
    for suffix_cmp_ind in range(1, len(tar_str)):
        # 如果当前要匹配的前缀字符和后缀字符不一样
        # 此时fail_jump已经记录了当前前缀匹配失败后 下一个准备匹配的前缀字符位置
        # 即fail_jump[prefix_cmp_ind - 1]
        # 如果该位置的字符还是与后缀要匹配的不一样 则继续跳转到当前前缀字符前一位置在fail_jump中的值
        # 直到前缀字符位置为0 因为不能再回溯了
        while prefix_cmp_ind != 0 and tar_str[prefix_cmp_ind] != tar_str[suffix_cmp_ind]:
            prefix_cmp_ind = fail_jump[prefix_cmp_ind - 1]
        
        # 到这，根据前缀字符与后缀字符，有两种可能
        # 1. 匹配：则说明当前最长公共前后缀就是0～当前前缀字符位置，其长度为 当前前缀字符位置+1。
        #         匹配成功的话，前缀字符位置还需要加1，即下一个后缀字符准备匹配下一个前缀字符。
        # 2. 不匹配，而前缀字符位置已经为0了 不能再回溯了：则说明当前没有公共的前后缀 则当前位置的fail_jump值为0
        # 
        if tar_str[prefix_cmp_ind] == tar_str[suffix_cmp_ind]:
            # 匹配的话
            # 下一个后缀要匹配的 就是当前前缀字符的下一位了
            prefix_cmp_ind += 1
            # 而当前位置的fail_jump也是指向后一个字符匹配失败后 下一个要匹配的前缀字符
            # 这说明当前位置是匹配成功了的 其指向的位置也就是prefix_cmp_ind
            fail_jump[suffix_cmp_ind] = prefix_cmp_ind
    
    print("fail jump: {}".format(fail_jump))
    return fail_jump
        


        



# @lc code=end

