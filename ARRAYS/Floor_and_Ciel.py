class Solution:
    def Floor_and_Ceil(self, arr, x):
        floor=-1
        ciel=-1
        for i in range(len(arr)):
            if arr[i]<=x:
                floor=arr[i]
            elif arr[i]>x and ciel==-1:
                ciel=arr[i]
        return(floor,ciel)
arr = [3, 4, 4, 7, 8, 10]
obj = Solution()
print(obj.Floor_and_Ceil(arr,5))



'''(4, 7)'''