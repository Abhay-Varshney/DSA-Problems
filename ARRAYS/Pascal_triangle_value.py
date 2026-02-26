class Solution:
    def Pascal_triangle(self,r,c):
        n=r-1
        k=c-1
        result=1
        for i in range(1,k+1):
            result=result*(n-i+1)//i
        return result
obj=Solution()
print(obj.Pascal_triangle(5,3))


'''6'''