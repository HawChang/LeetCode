#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #return self.is_sym_recursive(root.left, root.right)
        return self.is_sym_stack(root)
    
    def is_sym_stack(self, root):
        stack = list()
        stack.append((root.left, root.right))
        while len(stack) > 0:
            node1, node2 = stack.pop()
            # 如果都是None 则True 下一个
            if node1 is None and node2 is None:
                continue

            # 只有一个None 则False
            if node1 is None or node2 is None:
                return False
        
            # 都不为None时
            # 如果当前点不同 则False
            if node1.val != node2.val:
                return False

            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
    
        return True
    
    def is_sym_recursive(self, node1, node2):
        # 如果都是None 则True
        if node1 is None and node2 is None:
            return True
        # 只有一个None 则False
        if node1 is None or node2 is None:
            return False
        
        # 都不为None时
        # 如果当前点不同 则False
        if node1.val != node2.val:
            return False
        
        return self.is_sym(node1.left, node2.right) and self.is_sym(node1.right, node2.left)

# @lc code=end

