# Method-1 (Brute Force)
class Solution:
    def Two_Sum(self,arr):
        target=int(input("Enter target: "))
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    return [i,j]
arr=[0,1,6,5,9,5,0,1,6]
obj=Solution()
print(obj.Two_Sum(arr))


'''Enter target: 14
[3, 4]'''



# Method-2
class Solution:
    def Two_Sum(self,arr):
        target=int(input("Enter target: "))
        result={}
        for i in range(len(arr)):
            remaining=target-arr[i]
            if remaining in result:
                return [result[remaining],i]
            result[arr[i]]=i
arr=[0,1,6,5,9,5,0,1,6]
obj=Solution()
print(obj.Two_Sum(arr))



'''Enter target: 14
[3, 4]'''