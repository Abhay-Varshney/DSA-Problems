class Solution:
    def Single_element(self, arr):
        count=0
        for i in range(len(arr)):
            count ^=arr[i]
        return count
arr = [3,3,5,5,7]
obj = Solution()
print(obj.Single_element(arr))


'''7'''