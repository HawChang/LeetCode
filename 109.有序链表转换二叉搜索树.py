#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_length(cur_head):
            length = 0
            while cur_head is not None:
                cur_head = cur_head.next
                length += 1
            return length
        
        cur_head = head
        def build_tree(left, right):
            nonlocal cur_head
            # 如果left>right 则说明此处无节点
            if left > right:
                return None

            mid_num = (left + right + 1) // 2
            root = TreeNode(None)

            #中序遍历
            root.left = build_tree(left, mid_num - 1)

            # 到此访问根节点
            # 此时为根节点赋值 依次取链表的值即可
            root.val = cur_head.val
            cur_head = cur_head.next

            root.right = build_tree(mid_num + 1, right)

            return root

        length = get_length(head)
        #cur_root = TreeNode()
        # 中序遍历树的顺序 就是链表的顺序
        cur_root = build_tree(0, length - 1)
        return cur_root

# @lc code=end

