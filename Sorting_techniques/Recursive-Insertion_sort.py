class Solution:
    def Insertion_sort(self,arr,n):
        if n==1:
            return
        for i in range(n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return self.Insertion_sort(arr,n-1)
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
obj.Insertion_sort(arr,len(arr))
print(arr)


'''[1, 1, 5, 6, 9, 14, 21, 56]
'''