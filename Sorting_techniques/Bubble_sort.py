class Solution:
    def Bubble_sort(self):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
obj.Bubble_sort()


'''[1, 1, 5, 6, 9, 14, 21, 56]'''