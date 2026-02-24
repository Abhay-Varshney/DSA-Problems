class Solution:
    def longestSubarray(self, arr):
        cand1=cand2=None
        count1=count2=0
        for i in arr:
            if i==cand1:
                count1+=1
            elif i==cand2:
                count2+=1
            elif count1==0:
                cand1=i
                count1=1
            elif count2==0:
                cand2=i
                count2=1
            else:
                count1-=1
                count2-=1
        result = []
        if arr.count(cand1) > len(arr) // 3:
            result.append(cand1)
        if cand2 is not None and arr.count(cand2) > len(arr) // 3:
            result.append(cand2)
        return result
arr=[1, 2, 1, 1, 3, 2]
obj=Solution()
print(obj.longestSubarray(arr))



'''[1]'''