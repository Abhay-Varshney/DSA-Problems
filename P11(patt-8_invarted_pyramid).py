class Solution:
    def pattern(self):
        n=int(input('Enter no. of stars both row & column wise: '))
        for i in range(n,0,-1):
            for j in range(n-i):
                print(' ',end=' ')
            for k in range(2*i-1):
                print('*',end=' ')
            print()
obj=Solution()
obj.pattern()



'''Enter no. of stars both row & column wise: 5
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * '''