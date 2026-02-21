class Solution:
    def Best_time_to_buy_sell_stock(self, arr):
        min_price=arr[0]
        max_profit=0
        for i in arr:
            min_price=min(min_price,i)
            max_profit=max(max_profit,i-min_price)
        return max_profit
arr=[10,7,5,8,11,9]
obj=Solution()
print(obj.Best_time_to_buy_sell_stock(arr))



'''6'''