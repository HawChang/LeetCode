#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        return self.count_recursive(root, targetSum)
    
    def count_recursive(self, root, targetSum):
        path_num = 0
        def dfs(cur_node, sum_list=None):
            nonlocal path_num
            if cur_node is None:
                return

            if sum_list is None:
                sum_list = list()

            new_sum_list = list()
            # 0是加上自身点
            for cur_sum in sum_list + [0]:
                new_sum = cur_sum + cur_node.val
                if new_sum == targetSum:
                    path_num += 1
                new_sum_list.append(new_sum)
                

            dfs(cur_node.left, new_sum_list)
            dfs(cur_node.right, new_sum_list)
        
        dfs(root)
            
        return path_num

                

# @lc code=end

