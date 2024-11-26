from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLen = count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
            else:
                count = 1

            maxLen = max(count, maxLen)

        return maxLen

