class Solution:
    def Fibonacci_number(self,n):
        if n==0:
            return 0
        if n==1:
            return 1
        return self.Fibonacci_number(n-1)+self.Fibonacci_number(n-2)
obj=Solution()
print(obj.Fibonacci_number(7))


'''13'''