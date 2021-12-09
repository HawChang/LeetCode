#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        num_ind = 0
        def build_tree(left, right):
            nonlocal num_ind
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            # 中序遍历
            root.left = build_tree(left, mid - 1)

            # 遍历到当前根节点 
            # 赋值
            root.val = nums[num_ind]
            num_ind += 1

            root.right = build_tree(mid + 1, right)
            
            return root
        
        root = build_tree(0, len(nums) - 1)
        return root


# @lc code=end

