#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #return self.traverse_recursive(root)
        return self.traverse_with_stack(root)
    
    def traverse_with_stack(self, root):
        res_list = list()
        stack = list()
        stack.append(root)
        while len(stack) > 0:
            cur_node = stack.pop()
            if cur_node is not None:
                res_list.append(cur_node.val)
                stack.append(cur_node.right)
                stack.append(cur_node.left)
        return res_list
    
    def traverse_recursive(self, cur_node):
        res_list = list()
        if cur_node is not None:
            res_list.append(cur_node.val)
            res_list.extend(self.traverse_recursive(cur_node.left))
            res_list.extend(self.traverse_recursive(cur_node.right))
        return res_list

# @lc code=end

