class Solution:
    def Palindrome(self):
        n=int(input('Enter the Number: '))
        x=n
        rev=0
        while x>0:
            a=x%10
            rev=rev*10+a
            x=x//10
        if rev==n:
            print("palindrome")
        else:
            print("Not-Palindrome")
obj = Solution()
obj.Palindrome()



'''Enter the Number: 4566547
Not-Palindrome

Enter the Number: 4554
palindrome'''