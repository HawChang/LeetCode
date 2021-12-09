#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 按桶排序的思想安排任务
        # 有两种情况
        # 一种是有空余的间隔时间
        # 例如任务为A5B5C2D1，其安排结果可以是
        # ABC
        # ABC
        # ABD
        # ABX
        # AB
        # 注意：倒数第二行的X是优于A的间隔而必须空出来的
        # 倒数第一行的空白是不算在时间里的
        # 该种有空余间隔的情况，执行时间为(m-1)*(n+1)+c
        # 其中m表示最大的任务数，c表示最大任务数的任务有几个

        # 另一种是没有空余的间隔时间
        # 例如任务为A5B5C2D1F2，其安排结果可以是
        # ABCF
        # ABC
        # ABD
        # ABF
        # AB
        # 多出来的F是放在某桶里额外加一个 还是放在最后一行 都是没有影响的
        # 这种情况下 安排里已没有间隔 任务的量就是耗费的时间
        
        # 我们是可以不识别其到底能不能排满的
        # 任务安排按情况讨论
        # 1. 按安排方案没有空隔时间来算 此时执行时间t1=task_num。如果其实安排方案有间隔，则t1 <= t2
        # 2. 按安排方案有空隔时间来算 此时执行时间t2=(m-1)*(n+1)+c <= t。如果其实安排方案无间隔，则t2 <= t1
        # 对于同一堆任务来说，用两种方法得到的执行时间t1,t2
        # 取t1、t2中较大的即可
        # 当t1 < t2时，表示其实安排方案里有间隔时间
        # 当t1 > t2时，表示其实安排方案里没有间隔时间,t2少算了除最大任务数任务的其他任务

        task_count = collections.defaultdict(int)
        
        max_num = 0
        max_count = 0

        for cur_task in tasks:
            task_count[cur_task] += 1
            if task_count[cur_task] > max_num:
                max_num = task_count[cur_task]
                max_count = 1
            elif task_count[cur_task] == max_num:
                max_count += 1
        
        return max(len(tasks), (max_num - 1)*(n + 1) + max_count)


# @lc code=end

