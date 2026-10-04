# 2 sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen=dict()
        for item,i in enumerate(len(nums)):
            c=target-item
            if c in seen:
                return [i,seen[c]]

            else:
                seen[item]=i