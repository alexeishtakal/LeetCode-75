class Solution:
    def bs(self, potions, success, spell):
        potion_needed = (success + spell - 1) // spell
        l = 0
        r = len(potions)
        while l < r:
            mid = l + (r - l) // 2
            if potions[mid] >= potion_needed:
                r = mid
            else:
                l = mid + 1
        return l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions = sorted(potions)
        n = len(potions)
        for s in spells:
            pairs.append(n - self.bs(potions, success, s))
        return pairs
