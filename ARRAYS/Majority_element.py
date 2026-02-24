
class Solution:
    def Majority_element(self, arr):
        candidate = None
        count = 0

        for i in arr:
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1

        return candidate

                
arr=[0,1,6,5,9,5,0,1,6]
obj=Solution()
print(obj.Majority_element(arr))


'''6'''