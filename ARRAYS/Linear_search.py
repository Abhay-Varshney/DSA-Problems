class Solution:
    def Linear_search(self,arr):
        target=int(input('Enter element to find: '))
        for i in range(len(arr)):
            if arr[i]==target:
                return i
        return -1
arr=[1,0,4,7,0,3,8,0,0,6,0]
obj=Solution()
print(obj.Linear_search(arr))



'''Enter element to find: 6
    9
    
    
    Enter element to find: 9
    -1'''