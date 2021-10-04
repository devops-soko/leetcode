class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''

        count = 1
        start = False
        for c in s[1:] :
            if c == '(' :
                count +=1
            elif c == ')' :
                count -=1

            if count != 0 :
                if start:
                    start = False
                else :
                    result += c
            else :
                start = True
        return result