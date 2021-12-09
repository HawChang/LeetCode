#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #return self.groupAnagrams1(strs)
        return self.groupAnagrams2(strs)
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        group_dict = collections.defaultdict(list)
        for cur_str in strs:
            char_count = [0 for _ in range(26)]
            for cur_char in cur_str:
                key = ord(cur_char) - ord('a')
                char_count[key] += 1
            group_dict[tuple(char_count)].append(cur_str)

        return list(group_dict.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        group_dict = dict()
        for cur_str in strs:
            key = "".join(sorted(list(cur_str)))
            if key not in group_dict:
                group_dict[key] = list()
            group_dict[key].append(cur_str)

        return list(group_dict.values())

# @lc code=end

