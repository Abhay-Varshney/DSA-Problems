class Solution:
    def Second_Largest_Element(self,arr):
        largest=s_largest=float('-inf')
        for i in range(0,len(arr)):
            largest=max(largest,arr[i])
        for i in range(0,len(arr)):
            if arr[i]>s_largest and arr[i]!=largest:
                s_largest=arr[i]
        return s_largest
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
print(obj.Second_Largest_Element(arr))



'''21'''