class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a =string.ascii_lowercase
        d = {}
        for i,v in enumerate(l) :
            d[a[i]] = v

        result =[]
        for word in words:
            mose = ''
            for c in word:
                mose += d[c] 
            result.append(mose)
        return len(set(result))