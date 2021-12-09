#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = None
        def maxsum(cur_node):
            nonlocal max_sum
            if cur_node is None:
                return 0

            left_max = max(0, maxsum(cur_node.left))
            right_max = max(0, maxsum(cur_node.right))

            # 该节点作为顶点时的最大和
            # 该值作为递归时返回的值 用于其他节点求和中
            max_as_head = cur_node.val + max(left_max, right_max)

            # 该节点为路径最高点的最大和
            # 该值作为求路径和的值 用于最终结果的判断
            max_as_node = cur_node.val + left_max + right_max

            if max_sum is None or max_as_node > max_sum:
                max_sum = max_as_node
            
            return max_as_head
        
        maxsum(root)
        return max_sum


# @lc code=end

