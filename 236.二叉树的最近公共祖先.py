#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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
        #return self.lowestCommonAncestor1(root, p, q)
        return self.lowestCommonAncestor2(root, p, q)

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        #print("root: {}".format(root.val))

        if root == q or root == p:
            return root
        
        left_res = self.lowestCommonAncestor2(root.left, p, q)
        right_res = self.lowestCommonAncestor2(root.right, p, q)
        if left_res is not None and right_res is not None:
            return root
        elif left_res is not None:
            return left_res
        elif right_res is not None:
            return right_res
        else:
            return None

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        check_num = 0
        tar_dict = {p.val: None, q.val: None}

        def traverse(cur_node, cur_list):
            nonlocal tar_dict, check_num
            if cur_node is None:
                return

            cur_list = cur_list.copy() + [cur_node]

            if cur_node.val in tar_dict:
                tar_dict[cur_node.val] = cur_list
                check_num += 1
            
            if check_num < len(tar_dict):
                traverse(cur_node.left, cur_list)
                traverse(cur_node.right, cur_list)
        
        traverse(root, list())
        if check_num < len(tar_dict):
            return None

        prev_node = None

        p_path = tar_dict[p.val]
        q_path = tar_dict[q.val]
        print("p: {}".format([x.val for x in p_path]))
        print("q: {}".format([x.val for x in q_path]))

        max_ind = min(len(p_path), len(q_path))
        cur_ind = 0

        while cur_ind < max_ind:
            if p_path[cur_ind] != q_path[cur_ind]:
                break
            prev_node = p_path[cur_ind]
            cur_ind += 1
        
        return prev_node

        
# @lc code=end

