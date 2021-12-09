#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        #return self.numSquares1(n)
        return self.numSquares2(n)

    def numSquares2(self, n: int) -> int:
        # 任何正整数都能被表示为至多四个正整数的平方和
        # 当前仅当n = 4^k*(8m+7)时，n是四个正整数的平方和
        # n为一个正整数或两个正整数的平方和可以判断出来 若不是 则就是三个正整数了
        def is_perfect_square(num):
            return int(sqrt(num)) ** 2 == num
        
        def is_four_num_square_sum(num):
            # 将4^k去除
            while num % 4 == 0:
                num /= 4
            
            # 判断之后为8m+7
            return num % 8 == 7
        
        # 按判断的复杂程度来排序
        
        if is_perfect_square(n):
            return 1
        
        if is_four_num_square_sum(n):
            return 4
        
        # 判断是否能两个正整数
        cur_k = 1
        cur_square = cur_k ** 2
        # 只看一半就可以了
        half_n = n / 2.0
        while cur_square <= half_n:
            if is_perfect_square(n - cur_square):
                return 2
            cur_k += 1
            cur_square = cur_k ** 2
        
        return 3
        
    def numSquares1(self, n: int) -> int:
        dp = [0]
        for cur_n in range(1, n + 1):
            min_num = None
            cur_k = 1
            cur_square = cur_k ** 2
            while cur_square <= cur_n:
                cur_num = dp[cur_n - cur_square] + 1
                if min_num is None or cur_num < min_num:
                    min_num = cur_num
                cur_k += 1
                cur_square = cur_k ** 2
            dp.append(min_num)
        
        return dp[n]
        

# @lc code=end

