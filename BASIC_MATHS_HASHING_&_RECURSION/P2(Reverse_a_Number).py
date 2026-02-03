class Solution:
    def ReverseNumber(self):
        n=int(input('Enter the Number: '))
        x=n
        rev=0
        while x>0:
            a=x%10
            rev=rev*10+a
            x=x//10
        print(rev)
obj = Solution()
obj.ReverseNumber()



'''Enter the Number: 12345678
87654321'''