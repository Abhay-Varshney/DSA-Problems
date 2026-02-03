# Switch Statement

class Solution:
    def whichWeekDay(self):
        day=int(input('Enter Day Number'))
        match day:
            case 1:
                day='Monday'
            case 2:
                day='Tuesday'
            case 3:
                day='Wednesday'
            case 4:
                day='Thursday'
            case 5:
                day='Friday'
            case 6:
                day='Saturday'
            case _:
                day='Invalid Day'
        print(day)
w=Solution()
w.whichWeekDay()