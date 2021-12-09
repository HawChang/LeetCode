#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        cur_root = TreeNode(val=preorder[0])
        root_ind = inorder.index(cur_root.val)

        if root_ind > 0:
            cur_root.left = self.buildTree(
                preorder=preorder[1:root_ind + 1],
                inorder=inorder[:root_ind],
            )

        if root_ind < len(inorder) - 1:
            cur_root.right = self.buildTree(
                preorder=preorder[root_ind + 1:],
                inorder=inorder[root_ind + 1:],
            )
        return cur_root

# @lc code=end

