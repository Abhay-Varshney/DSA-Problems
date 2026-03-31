class Solution:
    def Max_Product_Subarray(self, arr):
        max_product = float('-inf')

        for i in range(len(arr)):
            product = 1
            for j in range(i, len(arr)):
                product *= arr[j]
                max_product = max(max_product, product)

        return max_product
arr = [1,2,-3,0,-4,-5]
obj = Solution()
print(obj.Max_Product_Subarray(arr))




'''20'''