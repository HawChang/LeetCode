#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:
        tree_list_table = [list() for _ in range(n + 1)]
        tree_list_table[0].append(None)
        # 个数从1到n
        for cur_num in range(1, n + 1):
            #print("cur_num: {}".format(cur_num))
            # 遍历当前个数下 可能分割的情况
            cur_tree_list = list()
            for split_ind in range(1, cur_num + 1):
                #print("split_ind: {}".format(split_ind))
                # 左侧范围[1, split_ind - 1]
                left_num = split_ind - 1
                # 右侧范围[split_ind + 1, n]
                right_num = cur_num - split_ind

                # 因为左侧的结果不做更改 因此这里不用单独克隆一遍
                # 这意味着 多个结果里的子树 可能存在同一个节点
                # 但这里不会出现问题
                left_tree_list = tree_list_table[left_num]
                #print("left num: {}, list size: {}".format(left_num, len(left_tree_list)))
                # 右侧相当于[1, n - split_ind] 偏移为split_ind
                # 右侧子树需要更改val 所以需要将table中的结果clone出来
                # 以免影响table中的节点
                right_tree_list = tree_list_table[right_num]
                #print("right num: {}, list size: {}".format(right_num, len(right_tree_list)))
                new_right_tree_list = list()
                for cur_right_tree in right_tree_list:
                    cur_right_tree = self.add_offset(cur_right_tree, split_ind)
                    new_right_tree_list.append(cur_right_tree)
                right_tree_list = new_right_tree_list
                #print("right num: {}, list size: {}".format(right_num, len(right_tree_list)))
                
                for cur_left_tree in left_tree_list:
                    for cur_right_tree in right_tree_list:
                        cur_tree = TreeNode(
                            val=split_ind,
                            left=cur_left_tree,
                            right=cur_right_tree,
                        )
                        cur_tree_list.append(cur_tree)
            
            #print("tree_list size: {}".format(len(cur_tree_list)))
            tree_list_table[cur_num] = cur_tree_list

        return tree_list_table[n]
    
    def add_offset(self, node, offset):
        if node is None:
            return None
        new_node = TreeNode(val=(node.val + offset))
        new_node.left = self.add_offset(node.left, offset)
        new_node.right = self.add_offset(node.right, offset)
        return new_node


# @lc code=end

