class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        length = len(s)
        while i < length -1 :
            if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                s=s[0:i] + s[i+2:]

                if i != 0:
                    i -= 1
                length -=2
                continue
            i +=1

        return s
