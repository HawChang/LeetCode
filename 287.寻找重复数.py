#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.findDuplicate1(nums)
        #return self.findDuplicate2(nums)

    def findDuplicate2(self, nums: List[int]) -> int:
        num_set = set(nums)
        return (sum(nums) - sum(num_set)) // (len(nums) - len(num_set))

    def findDuplicate1(self, nums: List[int]) -> int:
        # 有可能nums[i] = i 单元素成环
        # 但如果只有这一个i 则从数组其他部分 不会走到该出来
        # 且一开始nums[0] 不会等于0 所以不会走到一个单元素环中
        # 因此不存在误判

        # 又因为nums的长度为n+1 而数字的范围为[0,n]
        # 所以可以以数字直接找对应的nums元素 而不需要减1

        # 而如果有nums[i] = j. nums[j] = j
        # 则j处单元素成环 且有外部路径进入 此时也能通过检测环的存在来检测重复数字的存在

        # 一定有环 所以这里找环的入口 就是有两个入边的点
        # 该点的位置就是重复值 而不是该点的值
        
        s_p = 0
        f_p = 0

        while True:
            # 先走一次
            s_p = nums[s_p]
            f_p = nums[nums[f_p]]

            # 这里是比点相同 而不是里面的值相同
            if s_p == f_p:
                break
        
        s_p = 0
        while s_p != f_p:
            s_p = nums[s_p]
            f_p = nums[f_p]
        
        return s_p


# @lc code=end

