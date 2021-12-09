#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        cur_last_node = new_head
        prev_node = ListNode(val=None)
        prev_uniq = True

        cur_node = head
        while cur_node is not None:
            if prev_node.val != cur_node.val:
                if prev_node.val is not None and prev_uniq:
                    prev_node.next = None
                    cur_last_node.next = prev_node
                    cur_last_node = prev_node
                prev_node = cur_node
                prev_uniq = True
            else:
                prev_uniq = False

            cur_node = cur_node.next
        
        if prev_node.val is not None and prev_uniq:
            cur_last_node.next = prev_node
            prev_node.next = None
        
        return new_head.next


# @lc code=end

