#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #return self.canFinish1(numCourses, prerequisites)
        return self.canFinish2(numCourses, prerequisites)

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit_course = [False for _ in range(numCourses)]
        study_course = [False for _ in range(numCourses)]

        pre_dict = collections.defaultdict(list)
        for cur_course, pre_course in prerequisites:
            pre_dict[cur_course].append(pre_course)

        def study(course_ind):
            # 如果已学习过 则跳过
            if not study_course[course_ind]:
                # 如果没学习过 但访问过 说明依赖中有环 没有拓扑排序
                if visit_course[course_ind]:
                    return False
                # 开始尝试学习该课程
                # 记录该课程已访问
                visit_course[course_ind] = True
                # 学习其所有前置课程
                for pre_course in pre_dict[course_ind]:
                    if not study(pre_course):
                        return False
            
                study_course[course_ind] = True
            return True

        for cur_course_ind in range(numCourses):
            # 如果已经在stack中 则跳过
            if not study(cur_course_ind):
                return False
        
        return True


    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_edge = [0 for _ in range(numCourses)]
        # dependences[i] = [j1, j2, j3]，课程i是j1，j2，j3等课的先修
        dependences = collections.defaultdict(list)

        for pre_pair in prerequisites:
            cur_course, pre_course = pre_pair
            dependences[pre_course].append(cur_course)
            in_edge[cur_course] += 1
        
        #print("dep: {}".format(dependences))

        # 初始化的时候 将所有入度为0的课程加入队列
        queue = [x_ind for x_ind, x in enumerate(in_edge) if x == 0]

        study_num = 0
        while len(queue) > 0:
            #print("queue: {}".format(queue))
            # 取第一个 其实最后一个也没什么
            cur_course = queue.pop()
            study_num += 1
            # 将依赖该课的课程的入度减1 因为这门课已修
            for dependent_course in dependences[cur_course]:
                in_edge[dependent_course] -= 1
                if in_edge[dependent_course] == 0:
                    queue.append(dependent_course)
        
        return study_num == numCourses



# @lc code=end

