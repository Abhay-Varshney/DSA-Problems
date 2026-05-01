import math
class Solution:
    def Koko_Eating_Bananas(self, arr:list[int], h:int)-> int:
        low, high=1, max(arr)
        result=high
        while low<=high:
            mid=(low+high)//2
            total_hours=sum(math.ceil(pile/mid) for pile in arr)
            if total_hours<=h:
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result
arr=[25, 12, 8, 14, 19]
obj=Solution()
print(obj.Koko_Eating_Bananas(arr,5))
            
            
'''25'''