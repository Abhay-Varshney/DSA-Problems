# Method 1
class Solution:
    def Issorted(self,arr):
        new_arr=sorted(arr)
        if new_arr==arr:
            return True
        else:
            return False
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
print(obj.Issorted(arr))



'''False'''


# Method 2
class Solution:
    def Issorted(self,arr):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True
arr=[1,2,5,7,13,56,78]
obj=Solution()
print(obj.Issorted(arr))



'''True'''