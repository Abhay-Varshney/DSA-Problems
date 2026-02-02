class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(65+j),end=' ')
            print()
obj=Solution()
obj.pattern()



'''Enter no. of stars both row & column wise: 5
A B C D E 
A B C D 
A B C 
A B 
A 
'''