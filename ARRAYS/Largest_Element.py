class Solution:
    def Largest_Element(self,arr):
        largest=arr[0]
        for i in range(1,len(arr)):
            largest=max(largest,arr[i])
        return largest
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
print(obj.Largest_Element(arr))



'''56'''