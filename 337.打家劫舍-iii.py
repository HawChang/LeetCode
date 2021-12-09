#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        #return max(self.rob_recursive(root))
        return self.rob_dp(root)

    def rob_dp(self, root):
        rob_dict = dict()
        no_rob_dict = dict()
        rob_dict[None] = 0
        no_rob_dict[None] = 0

        def dfs(cur_node):
            if cur_node is None:
                return 

            dfs(cur_node.left)
            dfs(cur_node.right)

            rob_dict[cur_node] = cur_node.val + no_rob_dict[cur_node.left] + no_rob_dict[cur_node.right]
            no_rob_dict[cur_node] = max(rob_dict[cur_node.left], no_rob_dict[cur_node.left]) + \
                max(rob_dict[cur_node.right], no_rob_dict[cur_node.right])
            
        
        dfs(root)
        return max(rob_dict[root], no_rob_dict[root])
    
    def rob_recursive(self, cur_node):
        """返回当前节点打劫和不打劫两种情况下的最大值
        """
        if cur_node is None:
            return 0, 0

        left_no_rob_max, left_rob_max = self.rob_recursive(cur_node.left)
        right_no_rob_max, right_rob_max = self.rob_recursive(cur_node.right)
        
        cur_no_rob_max = max(left_no_rob_max, left_rob_max) + max(right_no_rob_max, right_rob_max)
        cur_rob_max = cur_node.val + left_no_rob_max + right_no_rob_max

        return cur_no_rob_max, cur_rob_max

# @lc code=end

