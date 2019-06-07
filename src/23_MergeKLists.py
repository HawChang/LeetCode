import heapq

# Definition for singly-linked list.


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class ListNodeComparable(ListNode):
	def __init__(self, other):
		self.next = other.next
		self.val  = other.val
		
	def __lt__(self,other):  # less than
		return self.val < other.val


class Solution:
	def mergeKLists(self, list_nodes) -> ListNode:
		root = ListNode(None)
		cur_root = root
		min_heap = list()
		# 首先将几个列表的头加入堆中
		for node in list_nodes:
			if node is not None:
				heapq.heappush(min_heap, ListNodeComparable(node))
		cur_node = heapq.heappop(min_heap) if len(min_heap) > 0 else None
		while cur_node is not None:
			# 将当前节点加入结果链表
			cur_root.next = ListNode(cur_node.val)
			cur_root = cur_root.next
			# 找到下一个节点
			if cur_node.next is not None:
				cur_node = heapq.heappushpop(min_heap, ListNodeComparable(cur_node.next))
			elif len(min_heap) > 0:
				cur_node = heapq.heappop(min_heap)
			else:
				cur_node = None
				
		return root.next


def display_list_node(head):
	cur_node = head
	info_list = list()
	while cur_node is not None:
		info_list.append(str(cur_node.val))
		cur_node = cur_node.next
	print("->".join(info_list))


if __name__ == "__main__":
	def create_from_list(src_list):
		root = ListNode(None)
		tmp_node = root
		for value in src_list:
			next_node = ListNode(value)
			tmp_node.next = next_node
			tmp_node = next_node
		return root.next
	
	def create_from_lists(src_lists):
		res = list()
		for cur_list in src_lists:
			res.append(create_from_list(cur_list))
		return res
	
		
	lists = [
		[1,4,5],
		[1,3,4],
		[2,6]
	]
	
	test_lists = create_from_lists(lists)
	display_list_node(test_lists[0])
	display_list_node(test_lists[1])
	display_list_node(test_lists[2])
	
	solution = Solution()
	head = solution.mergeKLists(test_lists)
	display_list_node(head)
