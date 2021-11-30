class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for edge in edges : 
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        for k,v in graph.items():
            if len(v) == len(edges):
                return k