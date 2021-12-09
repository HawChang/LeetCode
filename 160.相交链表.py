#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #return self.getIntersectionNode1(headA, headB)
        return self.getIntersectionNode2(headA, headB)

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB

        if p1 is None or p2 is None:
            return None

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

            if p1 is None and p2 is None:
                break

            if p1 is None:
                p1 = headB
            if p2 is None:
                p2 = headA
        
        return p1

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while True:
            if p1 is None and p2 is None:
                return p1

            if p1 is None:
                p1 = headB
            if p2 is None:
                p2 = headA

            if p1 == p2:
                return p1
            
            p1 = p1.next
            p2 = p2.next
        

# @lc code=end

