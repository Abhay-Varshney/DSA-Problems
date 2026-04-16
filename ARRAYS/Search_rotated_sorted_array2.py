class Solution:
    def How_many_times_array_rotated(self, arr,k):
        for i in range(len(arr)):
            if arr[i]==k:
                return True
        return False
arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
obj = Solution()
print(obj.How_many_times_array_rotated(arr,9))


'''False'''