class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        l = []
        for i in range(left, right+1) :
            l.append(i)
        for r in ranges:
            remove_list = []
            for v in l:
                if v >= r[0] and v <=r[1] :
                    remove_list.append(v)
            for v in remove_list:
                l.remove(v)
        if len(l) == 0:
            return True
        else:
            return False