class Solution:
    def Binary_Search(self, arr, target):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
arr = [-1,0,3,5,9,12]
obj = Solution()
print(obj.Binary_Search(arr, 9))



'''4'''