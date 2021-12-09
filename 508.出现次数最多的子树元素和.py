#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        node_sum_dict = collections.defaultdict(int)

        def dfs(cur_node):
            if cur_node is None:
                return 0
            
            cur_sum = cur_node.val + dfs(cur_node.left) + dfs(cur_node.right)
            node_sum_dict[cur_sum] += 1
            return cur_sum
        
        dfs(root)
        max_value = None
        max_sum_list = list()
        for cur_sum, cur_count in sorted(node_sum_dict.items(), key=lambda x:x[1], reverse=True):
            if max_value is None:
                max_value = cur_count

            if max_value != cur_count:
                break
            
            max_sum_list.append(cur_sum)
            
        print(node_sum_dict)
        return max_sum_list
        

# @lc code=end

