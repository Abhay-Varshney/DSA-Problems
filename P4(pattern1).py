class Solution:
    def pattern1(self):
        n=int(input('Enter no. of stars both row & column wise'))
        for i in range(n):
            for j in range(n):
                print('*',end=' ')
            print()
obj=Solution()
obj.pattern1()