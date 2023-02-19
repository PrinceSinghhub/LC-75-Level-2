class Solution:
    def maxProduct(self, nums):

        if len(nums) == 0:
            return 0

        # usining kandals Algo
        Max = nums[0]
        Min = nums[0]

        result = Max

        for i in range(1, len(nums)):
            current = nums[i]

            temp_max = max(current, Max * current, current * Min)

            Min = min(current, Max * current, current * Min)

            Max = temp_max

            result = max(result, Max)

        return result


