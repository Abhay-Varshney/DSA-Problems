class Solution:
    def MaxLen(self, arr):
        max_len=0
        for i in range(len(arr)):
            sum_ = 0
            for j in range(i, len(arr)):
                sum_ += arr[j]
                if sum_ == 0:
                    max_len = max(max_len, j - i + 1)
        return max_len
arr = [15, -2, 2, -8, 1, 7, 10, 23]
obj = Solution()
print(obj.MaxLen(arr))


'''5'''