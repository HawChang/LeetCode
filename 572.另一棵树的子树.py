#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        root_order = first_order(root)
        print("root order: {}".format(root_order))
        sub_root_order = first_order(subRoot)
        print("sub root order: {}".format(sub_root_order))

        fail_jump = gen_next(sub_root_order)

        p_pos = 0

        for cur_node in root_order:
            while p_pos != 0 and sub_root_order[p_pos] != cur_node:
                p_pos = fail_jump[p_pos - 1]
            
            if sub_root_order[p_pos] == cur_node:
                p_pos += 1
            
            if p_pos == len(sub_root_order):
                return True

        return False


def gen_next(s):
    fail_jump = [0 for _ in range(len(s))]

    p_cmp_ind = 0

    for s_cmp_ind in range(1, len(s)):
        while p_cmp_ind != 0 and s[p_cmp_ind] != s[s_cmp_ind]:
            p_cmp_ind = fail_jump[p_cmp_ind - 1]
        
        if s[p_cmp_ind] == s[s_cmp_ind]:
            p_cmp_ind += 1
        
        fail_jump[s_cmp_ind] = p_cmp_ind
    
    return fail_jump
    

def first_order(root):
    node_list = list()
    node_stack = list()
    node_stack.append(root)
    while len(node_stack) > 0:
        cur_node = node_stack.pop()
        if cur_node is None:
            node_list.append("None")
        else:
            node_list.append(cur_node.val)

            node_stack.append(cur_node.right)
            node_stack.append(cur_node.left)
    
    return node_list


# @lc code=end

