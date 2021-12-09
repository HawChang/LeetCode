#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
import random

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        quick_sort(people)
        #people = sorted(people, key=lambda x: (-x[0], x[1]))
        res = list()
        for cur_person in people:
            if cur_person[1] >= len(res):
                res.append(cur_person)
            else:
                res.insert(cur_person[1], cur_person)
        
        return res


def quick_sort(people):
    _quick_sort(people, 0, len(people) - 1)


def _quick_sort(people, left, right):
    if left < right:
        pivot = random_pivot(people, left, right)
        _quick_sort(people, left, pivot - 1)
        _quick_sort(people, pivot + 1, right)


def random_pivot(people, left, right):
    #print("left: {}, right: {}".format(left, right))
    rand_ind = random.randint(left, right)
    people[rand_ind], people[right] = people[right], people[rand_ind]

    cur_pivot = left
    for cur_ind in range(left, right):
        # cur_height > pivot 或者 cur_height == pivot and cur_order < pivot
        # 则在前
        if people[cur_ind][0] > people[right][0] \
                or (people[cur_ind][0] == people[right][0] and people[cur_ind][1] < people[right][1]):
            people[cur_ind], people[cur_pivot] = people[cur_pivot], people[cur_ind]
            cur_pivot += 1
        
    people[cur_pivot], people[right] = people[right], people[cur_pivot]
    #print("sort res: {}".format(people[left:right+1]))
    return cur_pivot
        

# @lc code=end

