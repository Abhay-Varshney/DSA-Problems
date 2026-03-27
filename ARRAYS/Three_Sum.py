class Solution:
    def ThreeSum(self, arr):
        result=set()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if arr[i]+arr[j]+arr[k]==0:
                        triplets=sorted((arr[i],arr[j],arr[k]))
                        result.add(tuple(triplets))
        return list(result)
arr = [2, -2, 0, 3, -3, 5]
obj = Solution()
print(obj.ThreeSum(arr))



'''[(-3, -2, 5), (-3, 0, 3), (-2, 0, 2)]'''