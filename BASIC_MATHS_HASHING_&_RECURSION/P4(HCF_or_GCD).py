class Solution:
    def HCF_or_GCD(self):
        n1=int(input("Enter first no.: "))
        n2=int(input("Enter second no.: "))
        HCF=1
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                HCF=i
        print(HCF)
obj=Solution()
obj.HCF_or_GCD()



'''Enter first no.: 12
Enter second no.: 3
3'''