class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        result = []
        def check_info(nums : List[int]) : 
            for num in set(nums) :
                if num in d:
                    d[num] +=1
                else:
                    d[num] =1

        check_info(nums1)
        check_info(nums2)
        check_info(nums3)

        for k,v in d.items() :
            if v !=1 :
                result.append(k)
        return result