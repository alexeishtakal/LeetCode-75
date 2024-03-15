class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])
        rotten = deque()
        fresh_count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh_count+=1
        minute=0
        while fresh_count>0 and rotten:
            for _ in range(len(rotten)):
                x,y=rotten.popleft()
                for i, j in [(x+i_step, y+j_step) for i_step, j_step in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                    if 0 <= i < n and 0 <= j < m and grid[i][j] == 1:
                        fresh_count-=1
                        grid[i][j]=2
                        rotten.append((i,j))
            minute+=1
        if fresh_count==0:
            return minute
        else:
            return -1