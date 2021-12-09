#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #return self.check_recursive(root)
        #return self.check_with_stack1(root)
        return self.check_with_stack2(root)

    def check_with_stack2(self, root):
        """迭代中序遍历
        """
        min_val = None
        stack = list()
        cur_node = root
        
        while len(stack) > 0 or cur_node is not None:
            if cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()

                if min_val is not None and cur_node.val <= min_val:
                    return False
                min_val = cur_node.val

                cur_node = cur_node.right

        return True
    
    def check_with_stack1(self, root):
        """迭代中序遍历
        """
        min_val = None
        stack = list()
        cur_node = root

        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        
        while len(stack) > 0:
            cur_node = stack.pop()
            if min_val is not None and cur_node.val <= min_val:
                return False
            
            min_val = cur_node.val
            cur_node = cur_node.right
            while cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left
        return True

    def check_recursive(self, root):
        """中序遍历 值应该递增
        """
        min_val = None

        def check(cur_node):
            nonlocal min_val
            if cur_node is None:
                return True
            if not check(cur_node.left):
                return False
            # 不满足则直接退出
            if min_val is not None and cur_node.val <= min_val:
                return False
            # 否则中序遍历到当前节点 当前节点即之后的最小值
            min_val = cur_node.val
            if not check(cur_node.right):
                return False
            # 满足所有才返回True
            return True
        
        return check(root)

    def isValidBST2(self, root: TreeNode) -> bool:
        stack = list()
        stack.append((root, None, None))
        res = True
        while len(stack) > 0:
            cur_node, min_val, max_val = stack.pop()
            if cur_node is None:
                continue
            if min_val is not None and min_val >= cur_node.val:
                res = False
                break
            if max_val is not None and max_val <= cur_node.val:
                res = False
                break
            stack.append((cur_node.left, min_val, cur_node.val))
            stack.append((cur_node.right, cur_node.val, max_val))
        
        return res

# @lc code=end

