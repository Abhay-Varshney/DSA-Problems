class Solution:
    def pattern(self):
        n = int(input('Enter number of rows: '))
        spaces = 2 * (n - 1)

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end='')

            for j in range(spaces):
                print(' ', end='')

            for j in range(i, 0, -1):
                print(j, end='')

            print()
            spaces -= 2


obj = Solution()
obj.pattern()



'''Enter number of rows: 5
1        1
12      21
123    321
1234  4321
1234554321'''