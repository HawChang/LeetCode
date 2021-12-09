#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start

class UnionFind:
    def __init__(self):
        self.father = dict()
        self.island_num = 0
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.island_num += 1
    
    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.island_num -= 1
    
    def find(self, x):
        if x not in self.father:
            return None

        final_ancestor = x
        while self.father[final_ancestor] is not None:
            final_ancestor = self.father[final_ancestor]
        
        while x != final_ancestor:
            origin_father = self.father[x]
            self.father[x] = final_ancestor
            x = origin_father
        
        return final_ancestor


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        uf = UnionFind()

        for cur_row in range(row):
            for cur_col in range(col):
                #print("cur_row: {}, cur_col:{}".format(cur_row, cur_col))
                cur_ind = cur_row * col + cur_col
                if grid[cur_row][cur_col] == "1":
                    uf.add(cur_ind)
                    if cur_col > 0 and grid[cur_row][cur_col - 1] == "1":
                        uf.merge(cur_ind, cur_ind - 1)
                    if cur_row > 0 and grid[cur_row - 1][cur_col] == "1":
                        uf.merge(cur_ind, cur_ind - col)
        
        return uf.island_num



# @lc code=end

