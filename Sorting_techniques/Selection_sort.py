class Solution:
    def Selection_sort(self):
        n=len(arr)
        for i in range(n):
            min=i
            for j in range(i+1,n):
                if arr[j]<arr[min]:
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
        print(arr)
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
obj.Selection_sort()


'''[1, 1, 5, 6, 9, 14, 21, 56]'''