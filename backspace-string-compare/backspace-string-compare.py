class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(sentence : str) -> str :
            result = ''
            for c in sentence:
                if c != '#':
                    result += c
                else:
                    if result != '':
                        result = result[:-1]
            return result
        if backspace(s) == backspace(t):
            return True
        else:
            return False