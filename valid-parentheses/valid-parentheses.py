class Solution:
    def isValid(self, s: str) -> bool:
        i =1
        length = len(s)
        while i < length  :
            if s[i] == ')' :
                if s[i-1] == '(' :
                    s = s[0:i-1] + s[i+1:]
                    if i !=1:
                        i -=1
                    length -=2
                    continue
            elif s[i] == ']' :
                if s[i-1] == '[' :
                    s = s[0:i-1] + s[i+1:]
                    if i !=1:
                        i -=1
                    length -=2
                    continue
            elif s[i] == '}' :
                if s[i-1] == '{' :
                    s = s[0:i-1] + s[i+1:]
                    if i !=1:
                        i -=1
                    length -=2
                    continue
            i+=1

        if s == '' :
            return True
        else:
            return False