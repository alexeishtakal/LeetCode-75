class Solution:
    def dfs(self, graph, x, y, visited):
        if x not in graph and y not in graph:
            return -1.0

        if y in graph[x]:
            return graph[x][y]

        for node in graph[x]:
            if node not in visited:
                visited.add(node)
                temp = self.dfs(graph, node, y, visited)
                if temp != -1.0:
                    return graph[x][node] * temp
        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
            graph[x][x] = 1.0
        print(graph)
        result = []
        for query in queries:
            visited = set()
            result.append(self.dfs(graph, query[0], query[1], visited))
        return result
