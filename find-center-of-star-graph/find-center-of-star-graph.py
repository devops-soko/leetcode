class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}
        for edge in edges :
            for n in edge:
                if n not in d:
                    d[n] = 1
                else:
                    d[n] +=1

        for k, v in d.items():
            if v == len(edges):
                return k