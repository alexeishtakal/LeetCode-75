class Solution:
    def dfs(self, graph, i, visited):
        for j in range(len(graph[i])):
            if graph[i][j]==1 and visited[j]==False:
                visited[j]=True
                self.dfs(graph, j, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)
        provinces = 0
        for i in range(len(isConnected)):
            if visited[i]==False:
                self.dfs(isConnected, i, visited)
                provinces+=1

        return provinces