class Solution:
    def makeGood(self, s: str) -> str:
        flag = True
        while flag:
            length = len(s)
            if length <=1 :
                break
            for i in range(0, length):
                if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    s=s[0:i] + s[i+2:]
                    break
                if i+1 >= length -1:
                    flag = False
                    break
        return s