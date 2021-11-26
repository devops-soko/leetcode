class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visted = set()
        d= collections.deque([start])
        while d:
            node = d.pop()
            if node == end:
                return True
            for child in graph[node] :
                if child not in d and child not in visted:
                    d.append(child)
            visted.add(node)
        return False