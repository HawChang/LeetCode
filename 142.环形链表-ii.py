#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow_point = head
        fast_point = head
        meet_point = None
        while fast_point is not None and fast_point.next is not None:
            slow_point = slow_point.next
            fast_point = fast_point.next.next
            if slow_point == fast_point:
                meet_point = head
                break
            
        if meet_point is None:
            return None
        else:
            while meet_point != slow_point:
                meet_point = meet_point.next
                slow_point = slow_point.next
            return meet_point
        
# @lc code=end

