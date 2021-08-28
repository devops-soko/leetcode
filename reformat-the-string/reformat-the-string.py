class Solution:
    def reformat(self, s: str) -> str:
        
        alpha = []
        digits = []
        for letter in s:
            if letter.isalpha():
                alpha.append(letter)
            else:
                digits.append(letter)
                
        answer = []
        useAlpha: bool = len(alpha) > len(digits)
        
        while True:
            if useAlpha:
                if not alpha:
                    break
                answer.append(alpha.pop())
            else:
                if not digits:
                    break
                answer.append(digits.pop())

            useAlpha = not useAlpha
        
        return answer if not alpha and not digits else ""