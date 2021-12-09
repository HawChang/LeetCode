#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
        """
        """
        if root is None:
            return
        # 逐层建立好next指针
        root.next = None
        leftmost = root
        prev_node = None
        
        def connect(cur_node):
            """层序遍历每一个节点
            """
            nonlocal prev_node, leftmost
            # 如果当前节点为空 则跳过
            if cur_node is None:
                return 

            # 如果当前层第一个节点还没有 则当前节点是第一个节点
            if leftmost is None:
                leftmost = cur_node
            
            # 如果当前节点有前序节点 则链接
            # 其实leftmost和prev_node一定是一个为None 另一个不为None
            # 可以只做一个判断 这里为了逻辑清晰 分开判断
            if prev_node is not None:
                prev_node.next = cur_node
            
            # 当前点记录为前一个节点
            prev_node = cur_node

        # 循环 直到当前层是最后一层
        while leftmost is not None:
            # 这里保证了下一层的存在
            cur_node = leftmost
            leftmost = None
            prev_node = None
            while cur_node is not None:
                connect(cur_node.left)
                connect(cur_node.right)
                cur_node =cur_node.next

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

