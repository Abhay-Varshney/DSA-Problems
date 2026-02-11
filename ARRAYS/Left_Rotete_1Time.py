# Method 1
class Solution:
    def Left_rotate_1Time(self,arr):
        temp=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[len(arr)-1]=temp
arr=[1,2,3,4,5]
obj=Solution()
obj.Left_rotate_1Time(arr)
print(arr)

'''[2, 3, 4, 5, 1]'''




# Method 2 (Only for python)
class Solution:
    def Left_rotate_1Time(self,arr):
        arr[:] = arr[1:] + arr[:1]
arr=[1,2,3,4,5]
obj=Solution()
obj.Left_rotate_1Time(arr)
print(arr)


'''[2, 3, 4, 5, 1]'''