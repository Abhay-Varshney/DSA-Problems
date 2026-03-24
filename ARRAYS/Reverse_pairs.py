class Solution:
    def Reverse_pairs(self, arr):
        count=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]>2*arr[j]:
                    count+=1
        return count
arr = [6, 4, 1, 2, 7]
obj = Solution()
print(obj.Reverse_pairs(arr))


'''3'''
