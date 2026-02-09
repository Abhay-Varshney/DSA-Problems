class Solution:
    def Quick_sort(self,arr,low,high):
        if low<high:
            p_index=self.Partition(arr,low,high)
            self.Quick_sort(arr,low,p_index-1)
            self.Quick_sort(arr,p_index+1,high)

        
    def Partition(self,arr,low,high):
        pivot=arr[low]
        i,j=low,high
        while i<j:
            while arr[i]<=pivot and i<=high-1:
                i+=1
            while arr[j]>=pivot and j>=low+1:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
obj.Quick_sort(arr,0,len(arr)-1)
print(arr)



'''[1, 1, 5, 6, 9, 14, 21, 56]'''