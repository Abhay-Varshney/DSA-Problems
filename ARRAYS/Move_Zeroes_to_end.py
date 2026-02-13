class Solution:
    def Move_zeroes_to_end(self,arr):
        temp=[]
        for i in range(len(arr)):
            if arr[i]!=0:
                temp.append(arr[i])
        for i in range(len(temp)):
            arr[i]=temp[i]
        for i in range(len(temp),len(arr)):
            arr[i]=0
arr=[1,0,4,7,0,3,8,0,0,6,0]
obj=Solution()
obj.Move_zeroes_to_end(arr)
print(arr)



'''[1, 4, 7, 3, 8, 6, 0, 0, 0, 0, 0]'''