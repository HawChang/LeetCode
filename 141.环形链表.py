#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #return self.hasCycle1(head)
        #return self.hasCycle2(head)
        return self.hasCycle3(head)

    def hasCycle3(self, head: ListNode) -> bool:
        slow_point = head
        fast_point = head
        while fast_point is not None and fast_point.next is not None:
            slow_point = slow_point.next
            fast_point = fast_point.next.next
            if slow_point == fast_point:
                return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow_point = head
        fast_point = head.next

        while slow_point != fast_point:
            if fast_point is None or fast_point.next is None:
                return False
            slow_point = slow_point.next
            fast_point = fast_point.next.next

        return True

    def hasCycle1(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow_point = head
        fast_point = head.next

        def step(src_point, step_num, tar_point=None):
            while src_point is not None and step_num != 0:
                # 从step一开始 就判断src_point是否等于tar_point
                if tar_point is not None and src_point == tar_point:
                    return True, src_point

                src_point = src_point.next
                step_num -= 1
            
            return False, src_point
        
        while fast_point is not None:
            check_res, fast_point = step(fast_point, 2, slow_point)
            if check_res:
                return True
            _, slow_point = step(slow_point, 1)

        
# @lc code=end

