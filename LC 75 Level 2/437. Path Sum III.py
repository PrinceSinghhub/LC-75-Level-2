# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            c = self.helper(root, sum)  # start from the root
            l = self.pathSum(root.left, sum)  # inside the left subtree
            r = self.pathSum(root.right, sum)  # inside the right subtree
            return c + l + r
        return 0

    def helper(self, root, sum):
        if root:
            l = self.helper(root.left, sum - root.val)
            r = self.helper(root.right, sum - root.val)
            return l + r + (root.val == sum)
        return 0
