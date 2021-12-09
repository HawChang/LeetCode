#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        head = TreeNode(left=root)
        next_depth = 1
        node_list = [head]
        while len(node_list) > 0 and next_depth < depth:
            next_node_list = list()
            for cur_node in node_list:
                if cur_node.left is not None:
                    next_node_list.append(cur_node.left)
                if cur_node.right is not None:
                    next_node_list.append(cur_node.right)
            next_depth += 1
            node_list = next_node_list
        
        if next_depth == depth:
            for cur_node in node_list:
                # 添加一层 不管左右节点是不是None
                new_node = TreeNode(val=val, left=cur_node.left)
                cur_node.left = new_node

                new_node = TreeNode(val=val, right=cur_node.right)
                cur_node.right = new_node

        return head.left

# @lc code=end

