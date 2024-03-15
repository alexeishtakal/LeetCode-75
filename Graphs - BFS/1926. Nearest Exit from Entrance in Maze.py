class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        from collections import deque
        queue = deque()
        queue.append((entrance, 0))
        maze[entrance[0]][entrance[1]] = '+'
        n = len(maze)
        m = len(maze[0])
        results = []
        while len(queue) > 0:
            current_cell = queue.popleft()
            i = current_cell[0][0]
            j = current_cell[0][1]
            if i - 1 == -1 or i + 1 == n or j - 1 == -1 or j + 1 == m:
                if current_cell[1] > 0:
                    results.append(current_cell[1])
                if current_cell[1] == n - i or current_cell[1] == m - j:
                    break

            if i - 1 >= 0 and maze[i - 1][j] == '.':
                queue.append(([i - 1, j], current_cell[1] + 1))
                maze[i - 1][j] = '+'

            if i + 1 < n and maze[i + 1][j] == '.':
                queue.append(([i + 1, j], current_cell[1] + 1))
                maze[i + 1][j] = '+'

            if j - 1 >= 0 and maze[i][j - 1] == '.':
                queue.append(([i, j - 1], current_cell[1] + 1))
                maze[i][j - 1] = '+'

            if j + 1 < m and maze[i][j + 1] == '.':
                queue.append(([i, j + 1], current_cell[1] + 1))
                maze[i][j + 1] = '+'

        if len(results) > 0:
            return min(results)
        else:
            return -1

