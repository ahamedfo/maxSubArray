class Solution(object):
    def maxSubArray(self, nums):
        opt = {}
        opt[0] = nums[0]
        max_sum_num = nums[0]

        for i in range(1, len(nums)):
            opt[i] = max(opt[i - 1] + nums[i], nums[i])
            if opt[i] > max_sum_num:
                max_sum_num = opt[i]

        return max_sum_num
        """
        :type nums: List[int]
        :rtype: int
        """

