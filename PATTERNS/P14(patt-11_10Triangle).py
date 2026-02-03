class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        for i in range(n):
            if i%2==0:
                start=1
            else:
                start=0
            for j in range(i+1):
                print(start,end=' ')
                start=1-start
            print()
obj=Solution()
obj.pattern()



'''Enter no. of stars both row & column wise: 6
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 '''