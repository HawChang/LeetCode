#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        leaf_num = 1
        for cur_val in preorder.split(","):
            # 槽位为空 说明不能再接收任何节点
            if leaf_num == 0:
                return False

            if cur_val == "#":
                leaf_num -= 1
            else:
                leaf_num += 1
        
        if leaf_num > 0:
            return False
        return True
# @lc code=end

