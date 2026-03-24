class Solution:
    def Count_invarsions(self, arr):
        count=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if i<j and arr[i]>arr[j]:
                    count+=1
        return count
arr = [2, 3, 7, 1, 3, 5]
obj = Solution()
print(obj.Count_invarsions(arr))


'''5'''