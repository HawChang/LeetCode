#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.convert_stack(root)
        #self.convert_recursive(root)
        return root
    
    def convert_stack(self, root):
        stack = list()
        cur_node = root

        total_sum = 0
        while len(stack) > 0 or cur_node is not None:
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.right
            else:
                cur_node = stack.pop()

                total_sum += cur_node.val
                cur_node.val = total_sum

                cur_node = cur_node.left
    
    def convert_recursive(self, root):
        node_list = list()
        def mid_rev_tranverse(cur_node):
            nonlocal node_list
            if cur_node is None:
                return
            mid_rev_tranverse(cur_node.right)
            node_list.append(cur_node)
            mid_rev_tranverse(cur_node.left)
        
        mid_rev_tranverse(root)
        print("node_list : {}".format([x.val for x in node_list]))
        
        total_sum = 0
        for cur_node in node_list:
            total_sum += cur_node.val
            cur_node.val = total_sum


# @lc code=end

