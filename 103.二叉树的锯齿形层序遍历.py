#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res_list = list()

        cur_level = list()
        cur_level.append(root)
        # 遍历当层每个节点时 其左右节点的添加顺序
        cur_dir = 1

        while len(cur_level) > 0:
            cur_res_list = list()
            next_level = list()
            for cur_node in cur_level:
                if cur_node is None:
                    continue
                cur_res_list.append(cur_node.val)
                left_right_list = [cur_node.left, cur_node.right]
                next_level.extend(left_right_list[::cur_dir])
            
            cur_dir *= -1
            # 每次都会反向 所以这里必反转一次
            cur_level = next_level[::-1]
            if len(cur_res_list) > 0:
                res_list.append(cur_res_list)
        
        return res_list

        
# @lc code=end

