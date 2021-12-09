#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self._stack = list()
        self._min_stack = list()

    def push(self, val: int) -> None:
        self._stack.append(val)
        if len(self._min_stack) == 0:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(self._min_stack[-1], val))

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

