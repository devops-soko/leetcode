class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        flag = True
        start = 1
        while flag:
            i =start
            for j in range(len(nums)):
                i = i + nums[j]
                if i <= 0 : 
                    start +=1
                    break
                if j == len(nums)-1:
                    flag =False
        return start