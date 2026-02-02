class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        for i in range(n):
            for j in range(i+1):
                print(chr(65+n-i-1+j),end=' ')

            print()
obj=Solution()
obj.pattern()



'''Enter no. of stars both row & column wise: 5
E 
D E 
C D E 
B C D E 
A B C D E '''