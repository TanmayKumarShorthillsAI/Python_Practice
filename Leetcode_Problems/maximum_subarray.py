class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_till_now = -1e9
        curr_sum = 0

        for x in nums:
            if curr_sum <= 0:
                curr_sum = 0

            curr_sum += x

            if curr_sum >= max_till_now:
                max_till_now = curr_sum

        return max_till_now
