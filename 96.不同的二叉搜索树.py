#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        count = [None for _ in range(n + 1)]
        # 初始化节点数为0和1时
        count[0] = 1
        count[1] = 1
        # 从节点数为2开始
        for cur_count in range(2, n + 1):
            # 遍历将节点分为两个子树的方案 因为是二叉搜索树 所以切分只能按数组顺序切分
            # 且其实数组中具体什么数不会影响子数的情况数 只有节点个数会影响
            total_count = 0
            for split_ind in range(1, cur_count + 1):
                # split_ind为以第几个数做切分 范围[1, cur_count]
                # 所以左侧个数为 split_ind - 1
                # 所以右侧个数为 cur_count - split_ind
                # 左侧和右侧的方案数相乘 即当前切分的方案数
                total_count += count[split_ind - 1] * count[cur_count - split_ind]
            count[cur_count] = total_count
        
        return count[n]


# @lc code=end

