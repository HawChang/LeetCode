#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.sum_recursive(root)
        #return self.sum_stack(root)

    def sum_stack(self, root):
        total_num = 0
        stack = list()
        stack.append((root, 0))
        while len(stack) > 0:
            cur_node, cur_sum = stack.pop()
            if cur_node is None:
                continue
            cur_sum = cur_sum * 10 + cur_node.val
            if cur_node.left is None and cur_node.right is None:
                total_num += cur_sum
            else:
                stack.append((cur_node.left, cur_sum))
                stack.append((cur_node.right, cur_sum))
        
        return total_num
    
    def sum_recursive(self, root):
        total_num = 0

        def recur(cur_node, cur_sum):
            nonlocal total_num
            # 遍历到为None的节点 该节点不为叶子节点 不是一条路径 该路忽略
            if cur_node is None:
                return
        
            cur_sum = cur_sum * 10 + cur_node.val
            if cur_node.left is None and cur_node.right is None:
                # 确定是叶子节点
                total_num += cur_sum
            else:
                # 子树递归
                recur(cur_node.left, cur_sum)
                recur(cur_node.right, cur_sum)
        
        recur(root, 0)
        return total_num
        

# @lc code=end

