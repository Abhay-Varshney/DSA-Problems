class Solution:
    def subarraySum(self, arr, k):
        prefix_sum = 0
        count = 0
        mp = {0: 1}   
        for num in arr:
            prefix_sum += num
            if prefix_sum - k in mp:
                count += mp[prefix_sum - k]
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
        return count
arr=[ 3, 7, 2, 5, 8, 4, 6, 0, 1]
obj=Solution()
print(obj.subarraySum(arr,10))



'''3'''