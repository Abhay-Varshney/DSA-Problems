class Solution:
    def Count_Occurence(self, arr, x):
        count=0
        for i in range(len(arr)):
            if arr[i]==x:
                count+=1
        return count
arr = [0, 0, 1, 1, 1, 1, 2, 3]
obj = Solution()
print(obj.Count_Occurence(arr,1))


'''4'''