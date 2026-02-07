class Solution:
    def Insertion_sort(self):
        n=len(arr)
        for i in range(n):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        print(arr)
arr=[5,6,1,9,21,56,14,1]
obj=Solution()
obj.Insertion_sort()



'''[1, 1, 5, 6, 9, 14, 21, 56]'''