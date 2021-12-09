#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = list()
        def dfs(cur_node):
            if cur_node is None:
                res.append('#')
            else:
                res.append(str(cur_node.val))
                dfs(cur_node.left)
                dfs(cur_node.right)
        
        dfs(root)
        #print("serilaize: {}".format(",".join(res)))
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #return self.deserialize1(data)
        return self.deserialize2(data)

    def deserialize2(self, data):
        val_list = data.split(",")
        cur_ind = 0

        def build_tree():
            nonlocal cur_ind
            if cur_ind == len(val_list):
                return None
            
            cur_char = val_list[cur_ind]
            cur_ind += 1
            
            if cur_char == '#':
                return None

            cur_node = TreeNode(cur_char)
            cur_node.left = build_tree()
            cur_node.right = build_tree()

            return cur_node
        
        return build_tree()

    def deserialize1(self, data):
        val_list = data.split(",")
        def build_tree(cur_ind):
            cur_node = None
            next_ind = None

            if cur_ind is not None and cur_ind != len(val_list):
                next_ind = cur_ind + 1
                if val_list[cur_ind] != '#':
                    cur_node = TreeNode(val_list[cur_ind])
                    cur_node.left, next_ind = build_tree(next_ind)
                    cur_node.right, next_ind = build_tree(next_ind)

            return cur_node, next_ind
        
        root, _ = build_tree(0)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

