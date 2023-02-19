class Solution:
    def permute(self, nums):

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        ans = []

        for i in range(len(nums)):
            m = nums[i]

            remLst = nums[:i] + nums[i + 1:]

            res = self.permute(remLst)
            for i in res:
                ans.append([m] + i)
        return ans

