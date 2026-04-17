class Solution:
    def Square_root(self,n):
        if n==0 or n==1:
            return n
        low,high=1,n
        result=1
        while low<=high:
            mid=(low+high)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                result=mid
                low=mid+1
            else:
                high=mid-1
        return result
n=7921
obj = Solution()
print(obj.Square_root(n))


'''89'''