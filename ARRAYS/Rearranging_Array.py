class Solution:
    def Rearranging_elements(self, arr):
        pos=[]
        neg=[]
        for i in arr:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        result=[]
        for j in range(len(pos)):
            result.append(pos[j])
            result.append(neg[j])
        return result
arr=[10,-7,-5,-8,11,9]
obj=Solution()
print(obj.Rearranging_elements(arr))



'''[10, -7, 11, -5, 9, -8]'''