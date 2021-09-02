class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result =1

        s = 0
        for num in nums:
            s += num
            if s <0 :
                result = max(abs(s)+1, result)

        return result
