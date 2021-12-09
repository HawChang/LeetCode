#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = list()
        stack.append(root)
        prev_node = None
        while len(stack) > 0:
            cur_node = stack.pop()
            if cur_node is None:
                continue
            if prev_node is not None:
                prev_node.left = None
                prev_node.right = cur_node
            prev_node = cur_node
            stack.append(cur_node.right)
            stack.append(cur_node.left)

# @lc code=end

