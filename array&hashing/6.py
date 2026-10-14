#Intersection of Two Arrays 349
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1)&set(nums2))
