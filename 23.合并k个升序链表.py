#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = list()
        for cur_ind, cur_node in enumerate(lists):
            if cur_node is not None:
                heappush(heap, (cur_node.val, cur_ind, cur_node))
        
        head = ListNode()
        cur_node = head
        
        while len(heap) > 0:
            _, cur_list_ind, cur_min_node = heappop(heap)
            cur_node.next = cur_min_node
            cur_node = cur_min_node
            
            if cur_min_node.next is not None:
                heappush(heap, (cur_min_node.next.val, cur_list_ind, cur_min_node.next))
        
        return head.next
            
        
# @lc code=end

