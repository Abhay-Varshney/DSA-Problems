class Solution:
    def Print_1toN(self,curr,n):
        if curr>n:
            return
        print(curr)
        self.Print_1toN(curr+1,n)

obj=Solution()
obj.Print_1toN(1,10)


''' 1
    2
    3
    4
    5
    6
    7
    8
    9
    10
'''