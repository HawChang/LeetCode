#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = list()
        cur_node = root
        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        
        prev_val = None
        min_diff = None
        while len(stack) > 0:
            cur_node = stack.pop()

            if prev_val is not None:
                cur_diff = cur_node.val - prev_val
                if min_diff is None or min_diff > cur_diff:
                    min_diff = cur_diff
            prev_val = cur_node.val

            cur_node = cur_node.right
            while cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
        
        return min_diff

    def getMinimumDifference2(self, root: TreeNode) -> int:
        stack = list()
        cur_node = root
        
        prev_val = None
        min_diff = None
        while len(stack) > 0 or cur_node is not None:
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()

                if prev_val is not None:
                    cur_diff = cur_node.val - prev_val
                    if min_diff is None or min_diff > cur_diff:
                        min_diff = cur_diff
                prev_val = cur_node.val

                cur_node = cur_node.right
        
        return min_diff


# @lc code=end

