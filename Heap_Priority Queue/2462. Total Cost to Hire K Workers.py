class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = costs[:candidates]
        qq = costs[max(candidates, len(costs)-candidates):]
        heapify(q)
        heapify(qq)
        total_cost=0
        i, ii = candidates, len(costs)-candidates-1
        for _ in range(k):
            if not qq or q and q[0]<=qq[0]:
                total_cost+=heappop(q)
                if i<=ii:
                    heappush(q, costs[i])
                    i+=1
            else:
                total_cost+=heappop(qq)
                if i<=ii:
                    heappush(qq, costs[ii])
                    ii-=1
        return total_cost