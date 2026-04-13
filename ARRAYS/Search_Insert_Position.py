class Solution:
    def Search_Insert_Position(self, arr, target):
        for i in range(len(arr)):
            if arr[i]==target:
                return i
            elif arr[i]>target:
                return i
arr = [1,3,5,6]
obj = Solution()
print(obj.Search_Insert_Position(arr,5))


'''2'''