#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #return self.removeNthFromEnd1(head, n)
        return self.removeNthFromEnd2(head, n)

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(next=head)
        f_node = root
        s_node = root
        while n > 0:
            f_node = f_node.next
            n -= 1

        prev_node = None
        while f_node is not None:
            prev_node = s_node
            f_node = f_node.next
            s_node = s_node.next
        
        prev_node.next = s_node.next
        
        return root.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        root = ListNode(next=head)
        def find_rev_k(cur_node, prev_node):
            if cur_node is None:
                cur_rev_rank = 0
            else:
                cur_rev_rank = find_rev_k(cur_node.next, cur_node) + 1
            
            if cur_rev_rank == n:
                prev_node.next = cur_node.next
            
            return cur_rev_rank
        
        find_rev_k(head, root)
        return root.next
            


# @lc code=end

