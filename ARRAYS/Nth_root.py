class Solution:
    def Nth_root(self,n,m)
        if n==0 or n==1:
            return n
        low,high=1,n
        result=1
        while low<=high:
            mid=(low+high)//2
            if mid**m==n:
                return mid
            elif mid**m<n:
                result=mid
                low=mid+1
            else:
                high=mid-1
        return result
n=216
obj = Solution()
print(obj.Nth_root(n,3))



'''6'''