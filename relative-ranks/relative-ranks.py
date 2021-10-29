class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        a = sorted(score, reverse=True)
        i = 0
        while i < len(a) : 
            if i == 0:
                d[a[i]] = "Gold Medal"
            elif i ==1 :
                d[a[i]] = "Silver Medal"
            elif i==2:
                d[a[i]] = "Bronze Medal"
            else:
                d[a[i]] = str(i+1)
            i +=1
        result = []
        for v in score :
            result.append(d[v])
        return result