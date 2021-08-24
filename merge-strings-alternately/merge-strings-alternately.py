class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for f,s in  zip(word1, word2) : 
            result += f+s
        w1_len, w2_len = len(word1), len(word2)
        if w1_len > w2_len :
            result += word1[w2_len-w1_len:]
        if w1_len < w2_len :
            result += word2[w1_len-w2_len:]
        return result