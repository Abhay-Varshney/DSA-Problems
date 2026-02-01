class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        for i in range(n,0,-1):
            for j in range(i):
                print('*',end=' ')
            print()
obj=Solution()
obj.pattern()


'''Enter no. of stars both row & column wise: 5
* * * * * 
* * * * 
* * * 
* * 
* '''