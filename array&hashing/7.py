#Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d={}
        ans=[]
        for item in nums1:
            d[item]=d.get(item,0)+1
        for item in nums2:
            if d.get(item,0)!=0:
                ans.append(item)
                d[item]-=1
        return ans

        