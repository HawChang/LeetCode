#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 遍历一遍链表 找到其最后一个节点 顺便可以确定该链表的长度
        list_size = 0
        last_node = None

        cur_node = head
        while cur_node is not None:
            list_size += 1
            last_node = cur_node
            cur_node = cur_node.next
        
        if list_size < 2:
            return head
        
        # 尾首相接
        last_node.next = head
        
        # 确认需要右移多少位
        sep_node_index = list_size - k % list_size
        #print("sep node index: {}".format(sep_node_index))
        cur_node = head
        for _ in range(sep_node_index - 1):
            cur_node = cur_node.next
        #print(cur_node.val)
        
        new_head = cur_node.next
        cur_node.next = None
        return new_head

        
# @lc code=end

