class Solution:
    def Longest_consecutive_sequence(self, arr):
        if not arr:
            return 0
        arr.sort()
        res = 1
        count = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1:
                count += 1
            elif arr[i] != arr[i-1]:
                count = 1
            res = max(res, count)
        return res
arr=[ 3, 7, 2, 5, 8, 4, 6, 0, 1]
obj=Solution()
print(obj.Longest_consecutive_sequence(arr))


'''9'''