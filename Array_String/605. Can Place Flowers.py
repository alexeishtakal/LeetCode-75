class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        free_pots = 0
        if len(flowerbed) > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                free_pots += 1
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                flowerbed[-1] = 1
                free_pots += 1
            for i in range(1, len(flowerbed) - 1):
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    free_pots += 1
                    flowerbed[i] = 1
        else:
            if flowerbed[0] == 0:
                free_pots += 1
        return free_pots >= n
