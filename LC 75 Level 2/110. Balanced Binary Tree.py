# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):

        self.answer = True

        def validate_tree(root):
            if not root:
                return 0
            left = validate_tree(root.left)
            right = validate_tree(root.right)

            if abs(left - right) > 1:
                self.answer = False
            return 1 + max(left, right)

        validate_tree(root)
        return self.answer