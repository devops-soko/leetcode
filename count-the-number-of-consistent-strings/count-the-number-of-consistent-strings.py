class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for word in words:
            for con in allowed :
                word = word.replace(con, '')
            if word == '' :
                result += 1
        return result