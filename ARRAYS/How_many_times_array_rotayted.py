class Solution:
    def How_many_times_array_rotated(self, arr):
        smallest=arr[0]
        index=0
        for i in range(len(arr)):
            if arr[i]<smallest:
                smallest=arr[i]
                index=i
        return index
arr = [4, 5, 6, 7, 0, 1, 2, 3]
obj = Solution()
print(obj.How_many_times_array_rotated(arr))


'''4'''