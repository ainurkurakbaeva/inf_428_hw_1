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

#     task2

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

#             task3

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = set(nums1)
        res = []
        for num in nums2:
            if num in hashmap and num not in res:
                res.append(num)

        return res