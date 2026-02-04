class Solution:
    def Armstrong(self):
        n=int(input("Enter no: "))
        x=n
        sum=0
        while x>0:
            a=x%10
            sum=sum+a**3
            x=x//10
        print(sum)
        if sum==n:
            print('Armstrong Number')
        else:
            print('Not-Armstrong Number')
obj=Solution()
obj.Armstrong()



'''Enter no: 153
153
Armstrong Number


Enter no: 421
73
Not-Armstrong Number
'''