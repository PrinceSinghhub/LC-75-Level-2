class Solution:

    def isSymmetric(self, root):
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:

            return False

        if left.val != right.val:
            return False
        a = self.check(left.left, right.right)
        b = self.check(left.right, right.left)

        return a and b