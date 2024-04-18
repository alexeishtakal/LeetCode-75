class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for v in arr:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1
        if len(d) == len(set([x for x in d.values()])):
            return True
        else:
            return False
