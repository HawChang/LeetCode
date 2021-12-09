#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        root = ListNode()
        cur_node = head
        # 将c插入r->n
        while cur_node is not None:
            # 记录c.next
            next_node = cur_node.next
            # 建立c->n
            cur_node.next = root.next
            # 建立r->c
            root.next = cur_node
            # 更新c
            cur_node = next_node
        return root.next
    

# @lc code=end

