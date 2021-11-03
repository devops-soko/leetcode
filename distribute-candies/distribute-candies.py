class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_type_len = len(set(candyType))
        edible_candy = len(candyType) // 2
        if candy_type_len >= edible_candy :
            return edible_candy
        else :
            return candy_type_len