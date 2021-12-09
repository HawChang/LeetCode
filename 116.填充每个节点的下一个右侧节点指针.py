#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #self.connect_hierarchically(root)
        self.connect_without_space(root)
        return root
    
    def connect_without_space(self, root):
        """因为是完美二叉树 所以不判断左右节点是否存在
        """
        if root is None:
            return
        # 逐层建立好next指针
        root.next = None
        leftmost = root
        # 循环 直到当前层是最后一层
        while leftmost.left is not None:
            # 这里保证了下一层的存在
            cur_node = leftmost
            while cur_node is not None:
                cur_node.left.next = cur_node.right
                if cur_node.next is not None:
                    cur_node.right.next = cur_node.next.left
                cur_node = cur_node.next

            # 下一层
            leftmost = leftmost.left


    def connect_hierarchically(self, root):
        cur_level = [root]
        while len(cur_level) > 0:
            prev_node = None
            next_level = list()
            for cur_node in cur_level:
                if cur_node is None:
                    continue
                if prev_node is not None:
                    prev_node.next = cur_node
                    cur_node.next = None
                prev_node = cur_node
                next_level.append(cur_node.left)
                next_level.append(cur_node.right)
            
            cur_level = next_level

        
# @lc code=end

