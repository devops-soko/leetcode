class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i, row in enumerate(mat) :
            d[i] = sum(row)

        s_d = sorted(d.items(), key=lambda x:(x[1], x[0]))

        result = []
        for i in range(k) :
            result.append(s_d[i][0])

        return result