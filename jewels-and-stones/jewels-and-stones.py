class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if len(jewels) < 1 or len(jewels) >50:
            return 
        if len(stones) < 1 or len(stones) >50:
            return 
        if not jewels.isalpha() or not stones.isalpha():
            return 
        if ''.join(sorted(jewels)) != ''.join(sorted(set(jewels))) :
            return
            
        output =0
        for jewel in jewels:
            output += stones.count(jewel)
        return output