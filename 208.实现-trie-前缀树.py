#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.children = dict()
        self.char = None
        self.word = None
        self.is_word = False

    def insert(self, word: str) -> None:
        cur_node = self
        for cur_char in word:
            if cur_char not in cur_node.children:
                new_node = Trie()
                new_node.char = cur_char
                cur_node.children[cur_char] = new_node
            cur_node = cur_node.children[cur_char]
        
        cur_node.is_word = True
        cur_node.word = word

    def search(self, word: str) -> bool:
        cur_node = self
        for cur_char in word:
            if cur_char not in cur_node.children:
                return False
            cur_node = cur_node.children[cur_char]
        return cur_node.is_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self
        for cur_char in prefix:
            if cur_char not in cur_node.children:
                return False
            cur_node = cur_node.children[cur_char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

