class Solution:
    def Lower_Bound(self, arr, x):
        for i in range(len(arr)):
            if arr[i]>=x:
                return i
        return len(arr)
arr = [1,2,2,3]
obj = Solution()
print(obj.Lower_Bound(arr,2))

'''1'''