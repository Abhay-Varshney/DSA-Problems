class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        num=1
        for i in range(n):
            for j in range(i+1):
                print(num,end=' ')
                num+=1
            print()
obj=Solution()
obj.pattern()




'''Enter no. of stars both row & column wise: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''