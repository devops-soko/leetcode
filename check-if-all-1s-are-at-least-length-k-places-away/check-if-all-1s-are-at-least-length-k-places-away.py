class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        start = False
        i =0
        for num in nums :
            if start :
                if num ==1 :
                    if i <k :
                        return False
                    i = 0
                else :
                    i += 1
            else :
                if num ==1 :
                    start = True
        return True