class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for word in words:
            for c in word :
                if c not in allowed :
                    result += 1
                    break
        return len(words) - result