class Solution:
    def CountDigits(self):
        n=int(input('Enter the Number: '))
        if n==0:
            return 1
        count=0
        while n>0:
            count+=1
            n=n//10
        print(count)
obj = Solution()
obj.CountDigits()



'''Enter the Number: 65432
5'''