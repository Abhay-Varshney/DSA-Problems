class Solution:
    def AllDivisors(self):
        n=int(input("Enter no: "))
        l=[]
        for i in range (1,n+1):
            if n%i==0:
                l.append(i)
                l.sort()
        print('List of all divisors: \n',l)
obj=Solution()
obj.AllDivisors()


'''Enter no: 120
List of all divisors: 
 [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
'''