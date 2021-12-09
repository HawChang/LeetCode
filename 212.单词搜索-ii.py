#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start

import collections 

class Trie(object):
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.is_word = False
        self.word = ""

    def insert(self, word):
        cur_node = self
        for cur_char in word:
            cur_node = cur_node.children[cur_char]
        
        cur_node.is_word = True
        cur_node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for cur_word in words:
            trie.insert(cur_word)
        
        row = len(board)
        assert row > 0
        col = len(board[0])

        word_set = set()
        visit = [[False for _ in range(col)] for _ in range(row)]
        def dfs(cur_node, cur_row, cur_col):
            if visit[cur_row][cur_col]:
                return

            cur_char = board[cur_row][cur_col]
            if cur_char in cur_node.children:
                next_node = cur_node.children[cur_char]
                # 确认当前节点是否单词
                if next_node.is_word:
                    word_set.add(next_node.word)
                # 根据当前节点继续往下找
                # 四周扩散
                next_pos_list = [
                    (cur_row - 1, cur_col), # 上
                    (cur_row + 1, cur_col), # 下
                    (cur_row, cur_col - 1), # 左
                    (cur_row, cur_col + 1), # 右
                ]
                # 往下找时 记录当前位置已被访问
                visit[cur_row][cur_col] = True
                for next_row, next_col in next_pos_list:
                    if 0 <= next_row < row and 0 <= next_col < col and not visit[next_row][next_col]:
                        dfs(next_node, next_row, next_col)
                # 当前位置确认完后 取消当前位置访问记录
                visit[cur_row][cur_col] = False
        
        for cur_row in range(row):
            for cur_col in range(col):
                dfs(trie, cur_row, cur_col)

        return list(word_set)
            


# @lc code=end

