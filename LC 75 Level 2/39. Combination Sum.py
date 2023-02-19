class Solution:

    def combinationSum(self, candidates, target):

        res = []
        path = []

        return self.findsum(candidates, target, res, path)

    def findsum(self, arr, target, res, path):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return

        for i in range(len(arr)):
            rem = target - arr[i]
            self.findsum(arr[i:], rem, res, path + [arr[i]])

        return res
