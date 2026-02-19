class Solution:
    def Leader_elements(self, arr):
        res=[]
        for i in range(len(arr)):
            is_leader=True
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    is_leader=False
                    break
            if is_leader:
                res.append(arr[i])
        return res
arr=[1,2,5,7,5,2,1]
obj=Solution()
print(obj.Leader_elements(arr))



'''[7, 5, 2, 1]'''