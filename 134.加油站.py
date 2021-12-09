#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        min_gas = None
        min_gas_pos = None
        res_gas = 0
        for cur_pos, (cur_gas, cur_cost) in enumerate(zip(gas, cost)):
            res_gas += cur_gas - cur_cost
            if min_gas is None or res_gas < min_gas:
                min_gas = res_gas
                min_gas_pos = cur_pos
                #print("min gas: {}, min_gas_pos: {}".format(min_gas, min_gas_pos))
        
        if res_gas < 0:
            return -1
        else:
            return (min_gas_pos + 1) % len(gas)


# @lc code=end

