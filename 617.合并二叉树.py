#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.merge_recursive(root1, root2)
    
    def merge_recursive(self, cur_node1, cur_node2):
        new_node = None
        if cur_node1 is None:
            if cur_node2 is not None:
                new_node = cur_node2
        else:
            if cur_node2 is None:
                new_node = cur_node1
            else:
                new_node = TreeNode(cur_node1.val + cur_node2.val)
                new_node.left = self.merge_recursive(cur_node1.left, cur_node2.left)
                new_node.right = self.merge_recursive(cur_node1.right, cur_node2.right)
        
        return new_node


# @lc code=end

