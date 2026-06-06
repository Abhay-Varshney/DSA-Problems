class Solution:
    def Consecutive_ones(self,arr):
        count=0
        max_count=0
        for i in range(len(arr)):
            if arr[i]==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        return max(max_count,count)
arr=[0,0,1,0,1,1,1,0,1,1,1,1,1,0]
obj=Solution()
print(obj.Consecutive_ones(arr))


'''5''