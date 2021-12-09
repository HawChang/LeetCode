#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start

class UnionFind:
    def __init__(self):
        self.father = dict()
        self.circle_num = 0
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.circle_num += 1
    
    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.circle_num -= 1
    
    def find(self, x):
        """查找x的祖先 顺便压缩其路径
        """
        # 找到祖先
        final_ancestor = x
        while self.father[final_ancestor] is not None:
            final_ancestor = self.father[final_ancestor]
        
        # 找到祖先后 x到祖先之间的节点 都指向该祖先
        while x != final_ancestor:
            origin_father = self.father[x]
            self.father[x] = final_ancestor
            x = origin_father
        
        return final_ancestor
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        city_num = len(isConnected)
        for cur_ind in range(city_num):
            uf.add(cur_ind)
            for other_ind in range(cur_ind):
                if isConnected[cur_ind][other_ind] == 1:
                    uf.merge(cur_ind, other_ind)
        
        return uf.circle_num


# @lc code=end