class Solution:
    def FourSum(self, arr, target):
        result=set()
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    for l in range(k+1, len(arr)):
                        if arr[i]+arr[j]+arr[k]+arr[l]==target:
                            quadraples=((arr[i],arr[j],arr[k],arr[l]))
                            result.add(tuple(quadraples))
        return list(result)
arr = [1, -2, 3, 5, 7, 9]
obj = Solution()
print(obj.FourSum(arr,7))


'''[(1, -2, 3, 5)]'''