#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        def left_max(cur_node):
            cur_node = cur_node.left
            while cur_node.right is not None:
                cur_node = cur_node.right
            return cur_node.val

        def right_min(cur_node):
            cur_node = cur_node.right
            while cur_node.left is not None:
                cur_node = cur_node.left
            return cur_node.val

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is not None:
                # 找前继节点 后继节点时即遍历到了下一个要删除节点
                # 之后还要从当前节点的子树再去找
                # 有重复操作
                root.val = left_max(root)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right is not None:
                root.val = right_min(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                return None
            
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = TreeNode(left=root)
        cur_node = root

        prev_node = head
        prev_dir = "left"
        
        def left_max(cur_node):
            nonlocal prev_node, prev_dir
            prev_node = cur_node
            prev_dir = "left"
            cur_node = cur_node.left
            while cur_node.right is not None:
                prev_node = cur_node
                prev_dir = "right"
                cur_node = cur_node.right
            return cur_node

        def right_min(cur_node):
            nonlocal prev_node, prev_dir
            prev_node = cur_node
            prev_dir = "right"
            cur_node = cur_node.right
            while cur_node.left is not None:
                prev_node = cur_node
                prev_dir = "left"
                cur_node = cur_node.left
            return cur_node

        def replace_node(cur_node):
            """从子树中找到一个节点替换到当前点来
            """
            nonlocal prev_node, prev_dir
            
            # 若不是叶子节点 则从子节点中 选被替换的节点
            if cur_node.left is not None:
                left_max_node = left_max(cur_node)
                cur_node.val = left_max_node.val
                replace_node(left_max_node)
            elif cur_node.right is not None:
                right_min_node = right_min(cur_node)
                cur_node.val = right_min_node.val
                replace_node(right_min_node)
            # 是叶子节点 则该点被删除即可
            else:
                setattr(prev_node, prev_dir, None)

        while cur_node is not None:
            if cur_node.val == key:
                replace_node(cur_node)
                break
            else:
                prev_node = cur_node
                if cur_node.val < key:
                    prev_dir = "right"
                    cur_node = cur_node.right
                else:
                    prev_dir = "left"
                    cur_node = cur_node.left
        
        return head.left
        

# @lc code=end

