#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        #return self.trap1(height)
        #return self.trap2(height)
        return self.trap3(height)
    
    def trap3(self, height):
        """左右指针
        """
        left_max = height[0]
        right_max = height[-1]

        left_ind = 0
        right_ind = len(height) - 1

        left_max = height[left_ind]
        right_max = height[right_ind]

        total = 0
        while left_ind <= right_ind:
            if left_max <= right_max:
                total += left_max - height[left_ind]
                left_ind += 1
                if left_ind <= right_ind:
                    left_max = max(left_max, height[left_ind])
            else:
                total += right_max - height[right_ind]
                right_ind -= 1
                if left_ind <= right_ind:
                    right_max = max(right_max, height[right_ind])
        
        return total
    
    def trap2(self, height):
        """单调栈 递减栈
        """
        stack = list()
        total = 0

        for cur_ind, cur_height in enumerate(height):
            # 栈中不保留 比cur_height矮的柱子
            while len(stack) > 0:
                top_ind, top_height = stack[-1]
                if top_height < cur_height:
                    # 栈顶弹出
                    stack.pop()
                    # 顺便计算雨水
                    # 如果栈中还有柱子 则计算积水
                    if len(stack) > 0:
                        left_ind, left_height = stack[-1]
                        depth = min(cur_height, left_height) - top_height
                        total += (cur_ind - left_ind - 1) * depth
                else:
                    break
                    
            stack.append((cur_ind, cur_height))
        
        return total

    def trap1(self, height):
        """过两遍 记录两侧最高值
        """
        left_max = 0
        right_max = 0
        left_height = [0 for _ in range(len(height))]
        right_height = [0 for _ in range(len(height))]

        for cur_ind in range(len(height)):
            if left_max < height[cur_ind]:
                left_max = height[cur_ind]
            left_height[cur_ind] = left_max

        for cur_ind in range(len(height) - 1, -1, -1):
            if right_max < height[cur_ind]:
                right_max = height[cur_ind]
            right_height[cur_ind] = right_max
        
        total = 0
        for cur_ind in range(len(height)):
            total += min(left_height[cur_ind], right_height[cur_ind]) - height[cur_ind]
            
        return total


# @lc code=end

