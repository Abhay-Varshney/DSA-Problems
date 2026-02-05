class Solution:
    def Sum_first_N_number(self,n):
        if n ==0:
            return 0
        return n+self.Sum_first_N_number(n-1)
obj=Solution()
print(obj.Sum_first_N_number(6))


'''21'''