# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, prev_sum):
            if not node: return 0

            cur_sum = 10 * prev_sum + node.val
            if not node.left and not node.right:
                return cur_sum

            return dfs(node.left, cur_sum) + dfs(node.right, cur_sum)

        return dfs(root, 0)
