class Solution:
    def Bubble_sort(self,arr,n):
        if n==1:
            return
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        self.Bubble_sort(arr,n-1)
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
obj.Bubble_sort(arr,len(arr))
print(arr)


'''[1, 1, 5, 6, 9, 14, 21, 56]'''