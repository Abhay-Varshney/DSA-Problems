class Solution:
    def Sort_0s_1s_2s(self, arr):
       low=0
       mid=0
       high=len(arr)-1
       while mid<=high:
            if arr[mid]==0:
               arr[low],arr[mid]=arr[mid],arr[low]
               low+=1
               mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
arr=[0,1,2,0,0,1,2,1,0,2,2,1]
obj=Solution()
obj.Sort_0s_1s_2s(arr)
print(arr)




'''[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]'''