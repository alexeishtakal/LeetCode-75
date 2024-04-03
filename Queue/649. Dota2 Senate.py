class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        for i in range(len(senate)):
            if senate[i] == "D":
                d.append(i)
            else:
                r.append(i)
        r = deque(r)
        d = deque(d)
        current_index = len(senate)
        while len(r) > 0 and len(d) > 0:
            if r[0] < d[0]:
                r.append(current_index)
            else:
                d.append(current_index)
            r.popleft()
            d.popleft()
            current_index += 1
        if len(d) > 0:
            return 'Dire'
        else:
            return 'Radiant'


