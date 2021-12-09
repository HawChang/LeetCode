#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start

class UnionFind:
    def __init__(self):
        self.father = dict()
        self.weight = dict()
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.weight[x] = 1.0
        
    def merge(self, x, y, val):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x]= root_y
            self.weight[root_x] = val * self.weight[y] / self.weight[x]
        else:
            assert self.weight[y] * val == self.weight[x]
    
    def find(self, x):
        final_ancestor = x
        while self.father[final_ancestor] is not None:
            final_ancestor = self.father[final_ancestor]

        children = list()
        while x != final_ancestor:
            origin_father = self.father[x]
            origin_weight = self.weight[x]
            self.weight[x] = 1.0
            self.father[x] = final_ancestor

            children.append(x)
            for cur_child in children:
                self.weight[cur_child] *= origin_weight

            x = origin_father

        return final_ancestor
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for cur_eq, cur_value in zip(equations, values):
            num_1, num_2 = cur_eq
            uf.add(num_1)
            uf.add(num_2)
            uf.merge(num_2, num_1, cur_value)
        
        res = list()
        for cur_query in queries:
            num_1, num_2 = cur_query
            cur_res = -1.0
            if num_1 in uf.father and num_2 in uf.father and uf.is_connected(num_1, num_2):
                cur_res = uf.weight[num_2] / uf.weight[num_1]
            res.append(cur_res)
        
        return res


# @lc code=end