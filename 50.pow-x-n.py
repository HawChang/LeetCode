#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return self.myPow1(x, n)
        return self.myPow2(x, n)

    def myPow2(self, x: float, n: int) -> float:
        def quick_mul(x, n):
            ans = 1.0

            cur_num = x
            cur_n = n

            while cur_n > 0:
                # 相当于判断cur_n最低位是0还是1
                # 此时对应着cur_num 如果为1 则说明cur_num应该在结果中 否则不在
                if cur_n % 2 == 1:
                    ans *= cur_num
                
                # 相当于n右移一位
                cur_n //= 2
                cur_num *= cur_num
            
            return ans
        
        return quick_mul(x, n) if n > 0 else 1 / quick_mul(x, -n)

    def myPow1(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow1(x, -n)

        divide_n = n // 2

        double_part = 1 if divide_n == 0 else self.myPow1(x, divide_n)
        single_part = 1 if n % 2 == 0 else x

        #print("divide_n: {}, double_part: {}".format(divide_n, double_part))

        return double_part * double_part * single_part

# @lc code=end

