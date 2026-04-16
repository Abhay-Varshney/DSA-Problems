class Solution:
    def Peak_element(self, arr):
        for i in range(len(arr)):
            if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                return i
arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
obj = Solution()
print(obj.Peak_element(arr))


'''7'''