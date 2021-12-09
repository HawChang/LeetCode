#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def depth(cur_node):
            if cur_node is None:
                return 0
            
            return max(
                depth(cur_node.left),
                depth(cur_node.right),
            ) + 1
        
        return depth(root)


# @lc code=end

