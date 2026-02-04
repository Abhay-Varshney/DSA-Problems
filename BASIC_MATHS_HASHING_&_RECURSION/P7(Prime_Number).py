class Solution:
    def Prime(self):
        n=int(input("Enter no: "))
        if n<2:
            print('Not Prime')
            return
        for i in range (2,n):
            if n%i==0:
                print('Not Prime')
                return
        print('Prime')
obj=Solution()
obj.Prime()



'''Enter no: 23
Prime

Enter no: 56
Not Prime
'''