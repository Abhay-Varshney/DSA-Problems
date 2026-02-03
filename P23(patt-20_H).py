class Solution:
    def pattern(self):
        n=int(input('Enter no.: '))
        for i in range(n-1):
            print("*"*(i+1) + " "*(2*(n-i-1)) + "*"*(i+1))
        for i in range(n):
            print("*"*(n-i) + " "*(2*i) + "*"*(n-i))


obj=Solution()
obj.pattern()


'''Enter no.: 7
*            *
**          **
***        ***
****      ****
*****    *****
******  ******
**************
******  ******
*****    *****
****      ****
***        ***
**          **
*            *'''