#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res_list = list()
        stack = list()
        stack.append((root, 0, list()))
        while len(stack) > 0:
            # 当前要加入路径的节点 和原路径的值
            cur_node, cur_val, cur_path = stack.pop()
            # 当前为空节点 不代表cur_path是到叶子节点的路径
            # 所以这里跳过就可以了
            if cur_node is None:
                continue
            
            next_val = cur_node.val + cur_val
            # 可能有小数val 所以不能剪枝
            #if next_val > targetSum:
            #    continue
            next_path = cur_path + [cur_node.val]

            if cur_node.left is None and cur_node.right is None:
                if next_val == targetSum:
                    res_list.append(next_path)
            else:
                # 可能压入空节点 所以之后弹出的时候 忽略掉空节点
                stack.append((cur_node.left, next_val, next_path))
                stack.append((cur_node.right, next_val, next_path))
        
        return res_list

        
# @lc code=end

