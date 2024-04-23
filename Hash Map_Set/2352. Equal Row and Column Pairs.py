class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = []
        columns = []
        rows = []
        for c in range(len(grid[0])):
            column = []
            for r in range(len(grid)):
                column.append(grid[r][c])
            columns.append(hash(str(column)))
            rows.append(hash(str(grid[c])))
        for r in range(len(rows)):
            for l in range(len(columns)):
                if rows[r] == columns[l]:
                    pairs.append([r, l])
        return len(pairs)

