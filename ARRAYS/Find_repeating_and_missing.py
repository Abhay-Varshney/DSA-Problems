class Solution:
    def Find_repeating_and_missing(self, arr):
        l=[0]*(len(arr)+1)
        for i in arr:
            l[i]+=1
            a=b=-1
            for i in range(1,len(arr)):
                if l[i]==2:
                    a=i
                elif l[i]==0:
                    b=i
        return [a,b]
arr = [3, 5, 4, 1, 1]
obj = Solution()
print(obj.Find_repeating_and_missing(arr))


'''[1, 2]'''