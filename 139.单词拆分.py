#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start

class Node():
    def __init__(self, char):
        self.children = dict()
        self.char = char
        self.is_word = False
        self.word = None 
    
    def find(self, tar_str):
        word_list = list()

        cur_node = self
        cur_ind = 0
        for cur_char in tar_str:
            if cur_char in cur_node.children:
                cur_node = cur_node.children[cur_char]
                if cur_node.is_word:
                    word_list.append(cur_node.word)
            else:
                break

        return word_list[::-1]
    
    def add(self, tar_str):
        cur_node = self
        for cur_char in tar_str:
            if cur_char not in cur_node.children:
                cur_node.children[cur_char] = Node(cur_char)
            cur_node = cur_node.children[cur_char]
        cur_node.is_word = True
        cur_node.word = tar_str


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #return self.wordBreak1(s, wordDict)
        return self.wordBreak2(s, wordDict)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        word_len_list = sorted(set([len(x) for x in wordDict]))
        word_set = set(wordDict)

        #dp[i]: [0, i-1]是否满足要求
        dp = list()
        # dp[0]满足要求
        dp.append(True)

        for cur_ind in range(len(s)):
            #print("ind: {}".format(cur_ind))
            # 检查s[0:cur_ind]范围下，能匹配后缀到的word
            check_res = False
            for cur_len in word_len_list:
                #print("len: {}".format(cur_len))
                if cur_len > cur_ind + 1:
                    break
                # 分为两部分[0, split_ind] [split_ind, cur_ind]
                split_ind = cur_ind - cur_len + 1 
                #print("check s[{}:{}]: {}".format(split_ind, cur_ind+1, s[split_ind: cur_ind+1]))
                if s[split_ind: cur_ind + 1] in word_set and dp[split_ind]:
                    #print("true")
                    # 此时dp长为
                    check_res = True
                    break
            dp.append(check_res)
        
        #print("dp: {}".format(dp))

        # dp长度应该是len(wordDict) + 1
        return dp[len(s)]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        #字典树+动态规划
        trie = Node("")
        for cur_word in wordDict:
            # 倒序添加 因为之后是倒序匹配
            trie.add(cur_word[::-1])
            #print("add: {}".format(cur_word[::-1]))

        #dp[i]: [0, i-1]是否满足要求
        dp = list()
        # dp[0]满足要求
        dp.append(True)

        for cur_ind in range(len(s)):
            # 检查s[0:cur_ind]范围下，能倒序匹配到的word
            check_res = False
            #print("cur_ind: {}, check: {}".format(cur_ind, s[cur_ind::-1]))
            for cur_word in trie.find(s[cur_ind::-1]):
                #print("word: {}".format(cur_word))
                # 对于匹配的word 还要查看剩下的部分 是否满足要求
                if dp[cur_ind - len(cur_word) + 1]:
                    #print("true")
                    check_res = True
                    break
            dp.append(check_res)
        
        #print("dp: {}".format(dp))
        
        # dp长度应该是len(wordDict) + 1
        return dp[len(s)]


# @lc code=end

