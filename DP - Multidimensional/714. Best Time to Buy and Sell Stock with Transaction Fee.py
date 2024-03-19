class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bought=-555555
        sold=0
        for price in prices:
            bought = max(bought, sold-price)
            sold = max(sold, bought+price-fee)
        return sold