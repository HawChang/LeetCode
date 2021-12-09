#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #return self.invert_recursive(root)
        return self.invert_stack(root)
    
    def invert_stack(self, root):
        if root is None:
            return None

        new_root = TreeNode(root.val)

        stack = list()
        stack.append((new_root, root))
        while len(stack) > 0:
            cur_new_node, cur_ori_node = stack.pop()
            if cur_ori_node.left is not None:
                cur_new_node.right = TreeNode(cur_ori_node.left.val)
                stack.append((cur_new_node.right, cur_ori_node.left))
            if cur_ori_node.right is not None:
                cur_new_node.left = TreeNode(cur_ori_node.right.val)
                stack.append((cur_new_node.left, cur_ori_node.right))
        return new_root
    
    def invert_recursive(self, cur_node):
        if cur_node is None:
            return None
        new_node = TreeNode(cur_node.val)
        new_node.left = self.invert_recursive(cur_node.right)
        new_node.right = self.invert_recursive(cur_node.left)
        return new_node


# @lc code=end

