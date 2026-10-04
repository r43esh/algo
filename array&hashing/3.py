#Contains Duplicate II leetocode=219
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen={}
        for i,item in enumerate(nums):
            if item in seen and abs(i-seen[item]) <=k:
                return True
            else:
                seen[item]=i

        return False