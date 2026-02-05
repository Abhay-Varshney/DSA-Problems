class Solution:
    def Recursion(self,n):
        if n==0:
            return
        print('Hello!!')
        self.Recursion(n-1)
obj=Solution()
obj.Recursion(5)


'''Hello!!
   Hello!!
   Hello!!
   Hello!!
   Hello!!
'''