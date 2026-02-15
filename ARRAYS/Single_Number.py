# Method-1 (Brute_Force)
class Solution:
    def Single_Number(self,arr):
        for i in range(len(arr)):
            num=arr[i]
            count=0
            
            for j in range(len(arr)):
                if arr[j]==num:
                    count+=1
                
            if count==1:
                return num
        return -1
arr=[0,1,6,5,9,5,0,1,6]
obj=Solution()
print(obj.Single_Number(arr))

'''9'''

# Method-2 
class Solution:
    def Single_Number(self,arr):
        count=0
        for i in arr:
            count^=i
        return count
arr=[0,1,6,5,9,5,0,1,6]
obj=Solution()
print(obj.Single_Number(arr))


'''9'''