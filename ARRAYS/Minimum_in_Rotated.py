class Solution:
    def Minimum_in_Rotated(self, arr):
        low=0
        high=len(arr)-1
        while low< high:
            mid=(low+high)//2
            if arr[mid]>arr[high]:
                low=mid+1
            else:
                high=mid
        return arr[low]
arr = [3, 4, 5, 1, 2]
obj = Solution()
print(obj.Minimum_in_Rotated(arr))


'''1'''