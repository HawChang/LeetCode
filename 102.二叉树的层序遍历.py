#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res_list = list()

        cur_level = list()
        cur_level.append(root)

        while len(cur_level) > 0:
            cur_res_list = list()
            next_level = list()
            for cur_node in cur_level:
                if cur_node is None:
                    continue
                cur_res_list.append(cur_node.val)
                next_level.append(cur_node.left)
                next_level.append(cur_node.right)

            cur_level = next_level
            # 最后一层可能为空
            if len(cur_res_list) > 0:
                res_list.append(cur_res_list)
        
        return res_list


# @lc code=end

