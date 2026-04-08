class Solution:
    def Merge_overlapping_subIntervals(self, interval):
        n=len(interval)
        visited=[False]*n
        result=[]
        
        for i in range(n):
            if visited[i]:
                continue
            s,e=interval[i]
            
            for j in range(i+1,n):
                if visited[j]:
                    continue
                s2,e2=interval[j]
                
                if not(e<=s2 or e2<=s):
                    s=min(s,s2)
                    e=max(e,e2)
                    visited[j]=True
            result.append([s,e])
            result.sort()
        return result
interval = [[1,5],[3,6],[8,10],[15,18]]
obj = Solution()
print(obj.Merge_overlapping_subIntervals(interal))


'''[[1, 6], [8, 10], [15, 18]]'''