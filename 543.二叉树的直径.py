#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_edge_num = 0

        def longest_edge(cur_node):
            nonlocal max_edge_num

            cur_depth = 0

            # 递归计算以该节点为最高点的最长路径
            if cur_node is not None:
                left_depth = longest_edge(cur_node.left)
                right_depth = longest_edge(cur_node.right)
                cur_depth = max(left_depth, right_depth) + 1
                cur_longest_edge = left_depth + right_depth

                # 更新最长路径
                if cur_longest_edge > max_edge_num:
                    max_edge_num = cur_longest_edge
            # 返回以当前点为最高点的最长路径
            return cur_depth
        
        longest_edge(root)
        return max_edge_num


# @lc code=end

