class Solution:
    def longestSubarray(self, arr, k):
        max_len = 0
        for i in range(len(arr)):
            curr_sum = 0
            for j in range(i, len(arr)):
                curr_sum += arr[j]
                if curr_sum == k:
                    max_len = max(max_len, j - i + 1)
        return max_len
arr=[10, 5, 2, 7, 1, 9]
obj=Solution()
print(obj.longestSubarray(arr,15))



'''4'''