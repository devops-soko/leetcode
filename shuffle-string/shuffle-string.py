class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_len, i_len = len(s), len(indices) 
        
        if s_len != i_len :
            return
        if s_len < 1 or s_len >100 :
            return
        if s != s.lower() :
            return
        if min(indices) != 0 or max(indices) != i_len-1 :
            return
        if i_len != len(set(indices)) :
            return
        
        d = {}
        for c,i in zip(s, indices) :
            d[i]=c
            
        output = ''
        for i in range(s_len):
            output += d[i]
        return output