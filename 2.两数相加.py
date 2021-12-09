#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(val=None, next=None)
        cur_node = head
        prev_inc = 0
        while l1 is not None or l2 is not None or prev_inc != 0:
            cur_l1_num = 0
            cur_l2_num = 0
            if l1 is not None:
                cur_l1_num = l1.val
                l1 = l1.next
            if l2 is not None:
                cur_l2_num = l2.val
                l2 = l2.next
            cur_num = cur_l1_num + cur_l2_num + prev_inc
            prev_inc = cur_num // 10
            cur_num %= 10
            cur_node.next = ListNode(val=cur_num, next=None)
            cur_node = cur_node.next
        
        return head.next


# @lc code=end