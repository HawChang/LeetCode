#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 找到第一个大于等于x的节点
        # 之后遇到小于x的节点都加在该点前
        new_head = ListNode(val=None, next=head)
        last_small_node = new_head
        last_big_node = None

        cur_node = head
        while cur_node is not None:
            if cur_node.val < x:
                # 还没有大于等于x的节点 则不做操作
                # 否则将该节点放到_left_node的后面
                if last_big_node is not None:
                    # 将该节点取出
                    last_big_node.next = cur_node.next
                    # 该节点插入到最后一个小于x的节点后面
                    cur_node.next = last_small_node.next
                    last_small_node.next = cur_node
                last_small_node = cur_node
            else:
                # 当前节点>=x
                last_big_node = cur_node

            cur_node = cur_node.next
        
        return new_head.next


# @lc code=end

