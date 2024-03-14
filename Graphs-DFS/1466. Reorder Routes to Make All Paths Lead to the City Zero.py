class Solution:
    def dfs(self, adj, visited, current_city, counter):
        visited[current_city] = True
        for neighbour_city in adj[current_city]:
            if not visited[neighbour_city[0]]:
                if neighbour_city[1] == 1:
                    counter +=1
                counter = self.dfs(adj, visited, neighbour_city[0], counter)
        return counter

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1],1))
            adj[connection[1]].append((connection[0],-1))
        visited = [False]*n
        counter=0
        counter = self.dfs(adj, visited, 0, counter)
        return counter