class Solution:
    def Merge_sort(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        left=self.Merge_sort(left)
        right=self.Merge_sort(right)
        return self.Merge_array(left,right)
        
        
    def Merge_array(self,left,right):
        result=[]
        i=j=0
        m=len(left)
        n=len(right)
        while i<m and j<n:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        
          #for checking if one array is exhausted.
        while i<m:
            result.append(left[i])
            i+=1
        
        while j<n:
            result.append(right[j])
            j+=1
        return result
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
print(obj.Merge_sort(arr))



'''[1, 1, 5, 6, 9, 14, 21, 56]'''