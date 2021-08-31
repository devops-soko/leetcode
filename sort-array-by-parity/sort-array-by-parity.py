class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_nums=[]
        even_nums=[]
        for num in nums:
            if num % 2 == 0:
                odd_nums.append(num)
            else :
                even_nums.append(num)

        return odd_nums + even_nums