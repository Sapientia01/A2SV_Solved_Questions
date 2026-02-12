# Questio link: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)

        distinct_nums1 = unique_nums1 - unique_nums2
        distinct_nums2 = unique_nums2 - unique_nums1

        return [list(distinct_nums1), list(distinct_nums2)]