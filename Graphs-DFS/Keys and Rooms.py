class Solution:

    def dfs(self, rooms, i, visited):
        if i not in visited:
            visited.add(i)
            for r in rooms[i]:
                self.dfs(rooms, r, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)