# If Else statements

class Solution:
    def studentGrade(self):
        marks = int(input('Enter Marks'))
        if marks >= 90:
            print('Grade A')
        elif marks >= 70:
            print('Grade B')
        elif marks >= 50:
            print('Grade C')
        elif marks >= 35:
            print('Grade D')
        else:
            print('Fail')


m = Solution()
m.studentGrade()