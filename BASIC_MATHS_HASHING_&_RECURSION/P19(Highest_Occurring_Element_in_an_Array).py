class Solution:
    def Counting_frequency(self):
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        max_freq=0
        result=float('inf')
        for i,count in freq.items():
            if count>max_freq or (count==max_freq and i<result):
                max_freq=count
                result=i
        print(result)
arr=[1,4,7,4,7,7,4,3,9,9,9,2,2,2]
obj=Solution()
obj.Counting_frequency()


'''2'''