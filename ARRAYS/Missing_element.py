class Solution:
    def Missing_element(self,arr):
        for i in range(len(arr)+1):
            if i not in arr:
                return i
arr=[2,0,3,4,5,1,8,7]
obj=Solution()
print(obj.Missing_element(arr))


'''6'''