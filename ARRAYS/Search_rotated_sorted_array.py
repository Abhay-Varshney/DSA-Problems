class Solution:
    def How_many_times_array_rotated(self, arr,k):
        for i in range(len(arr)):
            if arr[i]==k:
                return i
        return -1
arr = [4, 5, 0, 7, 8, 1, 2]
obj = Solution()
print(obj.How_many_times_array_rotated(arr,6))


'''-1'''