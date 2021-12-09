#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #return self.hammingDistance1(x, y)
        return self.hammingDistance2(x, y)

    def hammingDistance2(self, x: int, y: int) -> int:
        diff = x ^ y

        dist = 0

        while diff > 0:
            dist += diff & 1
            diff >>= 1
        
        return dist

    def hammingDistance1(self, x: int, y: int) -> int:
        diff = x ^ y

        dist = 0

        while diff > 0:
            dist += 1
            diff &= diff - 1
        
        return dist

# @lc code=end

