class Solution:
    def Counting_frequency(self):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        print(freq)
arr=[1,4,7,4,5,6,2,1,2,1,3]
obj=Solution()
obj.Counting_frequency()



'''{1: 3, 4: 2, 7: 1, 5: 1, 6: 1, 2: 2, 3: 1}'''