class Solution:
    def First_and_Last(self, arr, x):
        first=-1
        last=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==x:
                last=i
                break
        for i in range(len(arr)):
            if arr[i]==x:
                first=i
                break
        return [first,last]
arr = [5, 7, 7, 8, 8, 10]
obj = Solution()
print(obj.First_and_Last(arr,6))



'''[-1, -1]'''