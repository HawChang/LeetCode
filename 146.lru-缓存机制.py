#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start

class BiNode:
    def __init__(self, key, val=None, prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev = prev_node
        self.next = next_node
    
    def connect_2_sides(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = BiNode(key=None)
        self.tail = BiNode(key=None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_link(self, node_a, node_b):
        node_a.next = node_b
        node_b.prev = node_a
    
    def _add_node_after_head(self, cur_node):
        cur_node.connect_2_sides()
        # self.head.next 和 cur_node之间
        self._add_link(cur_node, self.head.next)
        self._add_link(self.head, cur_node)
    
    def _del_node_before_tail(self):
        cur_node = self.tail.prev
        cur_node.connect_2_sides()
        del self.cache[cur_node.key]

    def get(self, key: int) -> int:
        #print("get {}".format(key))
        if key in self.cache:
            cur_node = self.cache[key]
            # 该节点变为最近使用
            self._add_node_after_head(cur_node)
            return cur_node.val
        else:
            return -1
        #self.display()

    def put(self, key: int, value: int) -> None:
        #print("put {} -> {}".format(key, value))
        if key in self.cache:
            cur_node = self.cache[key]
            # 更新value
            cur_node.val = value
        else:
            # 新建节点
            cur_node = BiNode(key=key, val=value)
            self.cache[key] = cur_node
        
        # 该节点变为最近使用
        self._add_node_after_head(cur_node)
    
        # 如果capacity超过 则删除tail前的那个
        if self.capacity < len(self.cache):
            self._del_node_before_tail()

    
    #def display(self):
    #    cur_node = self.head.next
    #    res_list = list()
    #    while cur_node != self.tail:
    #        res_list.append((cur_node.key, cur_node.val))
    #        cur_node = cur_node.next
    #    print("res: {}".format(res_list))


        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

