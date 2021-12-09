#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #return self.traverse_recursive(root)
        #return self.traverse_with_stack(root)
        return self.traverse_with_stack2(root)
    
    def traverse_with_stack2(self, root):
        res_list = list()

        stack = list()
        cur_node = root

        # 对于一个没有访问过的节点
        # 将其所有左节点压栈
        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left

        while len(stack) > 0:
            # 压栈的节点的左节点一定访问了
            # 此时弹出 则访问自身 
            cur_node = stack.pop()
            res_list.append(cur_node.val)
            # 然后访问右节点
            # 访问新的节点的时候 也要将其所有左节点压栈
            cur_node = cur_node.right
            while cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
        
        return res_list

    def traverse_with_stack(self, root):
        res_list = list()

        stack = list()
        cur_node = root

        # 要么节点不为空 要么栈不为空
        while cur_node is not None or len(stack) > 0:
            # 如果当前节点不为空 将当前节点压栈 继续访问左节点
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                # 如果当前节点为空 
                # 说明当前栈顶节点的左子树节点不存在或访问完
                # 因此输出栈顶节点
                # 并将cur_node变为栈顶节点的右子节点
                # 下次循环时 会将该新节点的所有左子节点压入栈
                cur_node = stack.pop()
                res_list.append(cur_node.val)
                cur_node = cur_node.right
        
        return res_list
    
    def traverse_recursive(self, cur_node):
        res_list = list()
        if cur_node is not None:
            res_list.extend(self.traverse_recursive(cur_node.left))
            res_list.append(cur_node.val)
            res_list.extend(self.traverse_recursive(cur_node.right))
        return res_list

# @lc code=end

