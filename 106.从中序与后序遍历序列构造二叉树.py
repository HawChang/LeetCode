#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        cur_root = TreeNode(val=postorder[-1])
        root_ind = inorder.index(cur_root.val)

        if root_ind > 0:
            cur_root.left = self.buildTree(
                inorder=inorder[:root_ind],
                postorder=postorder[:root_ind],
            )
        
        if root_ind < len(inorder) - 1:
            cur_root.right = self.buildTree(
                inorder=inorder[root_ind + 1:],
                postorder=postorder[root_ind: -1],
            )
            
        return cur_root
        
# @lc code=end

