class Solution:
    def Print_Nto1(self,n):
        if n<1:
            return
        print(n)
        self.Print_Nto1(n-1)
obj=Solution()
obj.Print_Nto1(10)


''' 10
    9
    8
    7
    6
    5
    4
    3
    2
    1'''