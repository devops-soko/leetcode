class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left = 0
        while left < len(arr) :
            if arr[left] ==  0 :
                arr.pop()
                arr.insert(left, 0)
                left +=2
            else :
                left +=1