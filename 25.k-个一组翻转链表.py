#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = ListNode(next=head)
        cur_node = root

        # 重复cur_node之后的k个节点
        # 直到cur_node之后节点不足k个
        while cur_node is not None:
            #self.display(root.next)
            # 确认当前节点后是否存在k个节点
            cur_end_node = cur_node
            cur_size = 0
            while cur_end_node is not None and cur_size < k:
                cur_end_node = cur_end_node.next
                cur_size += 1
            
            if cur_end_node is not None:
                # 若存在 先确认该k个节点的前序和后序节点
                # 前序节点就是当前节点
                head_prev = cur_node
                # 后序节点就是最后节点的下一个
                tail_next = cur_end_node.next
                # 当前k个节点的第一个 就是前序节点的下一个
                cur_head = head_prev.next

                # k个节点依次翻转
                cur_rev_node = cur_head
                prev_rev_node = None
                # 翻转直到cur_end_node
                for _ in range(k):
                    # 下一个rev的节点
                    next_rev_node = cur_rev_node.next
                    # 更新当前节点对应的节点
                    cur_rev_node.next = prev_rev_node
                    # 更新下一次的翻转
                    prev_rev_node = cur_rev_node
                    cur_rev_node = next_rev_node
                
                # k个节点翻转完后 连接前序和后序节点
                # 前序节点连接头节点
                head_prev.next = prev_rev_node
                # 尾节点连接后序节点
                cur_head.next = tail_next
            
                # 当前尾节点作为下一次逆序的cur_node节点
                cur_node = cur_head
            else:
                break
        
        return root.next


# @lc code=end

