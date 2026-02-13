class Solution:
    def Union_array(self,arr1,arr2):
            result=[]
            i=j=0
            m=len(arr1)
            n=len(arr2)
            while i<m and j<n:
                if arr1[i]<=arr2[j]:
                    if len(result)==0 or result[-1]!=arr1[i]:
                        result.append(arr1[i])
                    i+=1
                else:
                    if len(result)==0 or result[-1]!=arr2[j]:
                        result.append(arr2[j])
                    j+=1
            
            #for checking if one array is exhausted.
            while i<m: 
                 if len(result)==0 or result[-1]!=arr1[i]:
                    result.append(arr1[i])
                    i+=1
            
            while j<n:
                if len(result)==0 or result[-1]!=arr2[j]:
                    result.append(arr2[j])
                    j+=1
            return result
arr1=[5,6,8,10]
arr2=[2,5,6]
obj=Solution()
print(obj.Union_array(arr1,arr2))


'''[2, 5, 6, 8, 10]'''