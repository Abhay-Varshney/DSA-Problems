class Solution:
    def Remove_Duplicate(self,arr):
        if len(arr)==1:
            return 1
        i=0
        j=i+1
        while j<len(arr):
            if arr[j]!=arr[i]:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
        return i+1
arr=[1,1,1,2,2,3,4,5,6]
obj=Solution()
print(obj.Remove_Duplicate(arr))



'''6'''