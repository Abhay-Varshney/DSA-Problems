class Solution:
    def Factorial(self,n):
        if n==0 or n==1:
            return 1
        return n*self.Factorial(n-1)
obj=Solution()
print(obj.Factorial(5))

'''120'''