class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i),end=' ')
            print()
obj=Solution()
obj.pattern()



'''Enter no. of stars both row & column wise: 5
A 
B B 
C C C 
D D D D 
E E E E E '''