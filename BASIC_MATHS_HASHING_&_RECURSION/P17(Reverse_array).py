class Solution:
    def Reverse_array(self,arr,l,r):
        if l>=r:
            return
        arr[l],arr[r]=arr[r],arr[l]
        self.Reverse_array(arr,l+1,r-1)
arr=[12,45,36,37,76]
obj=Solution()
obj.Reverse_array(arr,0,len(arr)-1)
print(arr)


'''[76, 37, 36, 45, 12]
'''