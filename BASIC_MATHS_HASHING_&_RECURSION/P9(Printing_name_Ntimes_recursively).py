class Solution:
    def Name(self,name,n):
        if n==0:
            return
        print(name)
        self.Name(name,n-1)
obj=Solution()
obj.Name('Abhay',5)


''' Abhay
    Abhay
    Abhay
    Abhay
    Abhay
'''