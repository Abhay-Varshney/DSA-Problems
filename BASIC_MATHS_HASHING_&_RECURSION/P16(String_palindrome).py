class Solution:
    def String_palindrome(self):
        s=input('Enter String: ')
        a=s[::-1]
        if a==s:
            print('Palindrome')
        else:    
            print('Not Plindrome')
obj=Solution()
obj.String_palindrome()


'''Enter String: malayalam
Palindrome



Enter String: knife
Not Plindrome'''