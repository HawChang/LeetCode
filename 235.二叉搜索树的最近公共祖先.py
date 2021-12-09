#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 其实不存在该情况 题中已说明p、q为不同节点 且不存在相同值的节点
        if p.val == q.val:
            return p

        if p.val < q.val:
            small_node = p
            big_node = q
        else:
            small_node = q
            big_node = p

        def check_status(cur_node):
            """节点分布情况:
            1. 两节点都在cur_node左侧
            2. 两节点都在cur_node右侧
            3. 两节点在cur_node两侧，或某节点就是cur_node
            情况1、2 节点继续下探
            情况3 找到最近公共祖先
            """
            if big_node.val < cur_node.val:
                return 1
            elif cur_node.val < small_node.val:
                return 2
            else:
                return 3

        cur_node = root
        cur_status = check_status(cur_node)

        common_ancestor = None

        while cur_node is not None:
            if cur_status == 1:
                cur_node = cur_node.left
            elif cur_status == 2:
                cur_node = cur_node.right
            elif cur_status == 3:
                common_ancestor = cur_node
                break
            cur_status = check_status(cur_node)
        
        return common_ancestor
            
        
# @lc code=end

