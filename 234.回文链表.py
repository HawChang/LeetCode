#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        # 找到重点
        s_p = head
        f_p = head
        prev_p = None
        # 结束时f_p可能为空 可能为最后一个节点
        # 若节点为偶数 则f_p为空
        # 若节点为奇数 则f_p为最后一个节点 
        while f_p is not None and f_p.next is not None:
            # 一开始时s_p和f_p是同一个节点
            # 要先走f_p
            # 后面s_p会更改节点的next值
            f_p = f_p.next.next

            # 将前半部分反转
            tmp_p = s_p.next
            s_p.next = prev_p
            # 记录上一个节点 也就是当前节点
            prev_p = s_p

            # 下一个慢节点
            s_p = tmp_p

        # f_p到末尾时
        # s_p是后半部分的起始。指向的是链表的中点(奇数)或中间的后一个点(偶数) n+1//2
        # 当f_p是最后一个节点是 说明该链表是奇数链表 s_p是链表中点
        # 此时s_p应前进一个 才能与prev_p比较
        if f_p is not None:
            s_p = s_p.next

        # prev_p是前半部分的起始。s_p的前一个
        while s_p is not None and prev_p is not None:
            if s_p.val != prev_p.val:
                return False
            s_p = s_p.next
            prev_p = prev_p.next
        
        return s_p is None and prev_p is None

        
# @lc code=end

