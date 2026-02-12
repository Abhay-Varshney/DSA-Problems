# Method 1
class Solution:
    def Left_rotate_K_Time(self,arr,k):
        rotation=k%len(arr)
        for i in range(0,rotation):
            x=arr.pop(0)
            arr.insert(len(arr),x)
arr=[1,2,3,4,5]
obj=Solution()
obj.Left_rotate_K_Time(arr,3)
print(arr)

'''[4, 5, 1, 2, 3]'''



# Method 2 (Only for Python)
class Solution:
    def Left_rotate_K_Time(self,arr,k):
        k=k%len(arr)
        arr[:]=arr[k:]+arr[:k]
arr=[1,2,3,4,5]
obj=Solution()
obj.Left_rotate_K_Time(arr,6)
print(arr)

'''[2, 3, 4, 5, 1]'''