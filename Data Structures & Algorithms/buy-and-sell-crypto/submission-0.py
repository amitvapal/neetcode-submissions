class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy + 1
        maxProf = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                currProf = prices[sell] - prices[buy]
                maxProf = max(maxProf, currProf)
                sell+=1
            elif prices[buy] >= prices[sell]:
                buy = sell
                sell+= 1
        return maxProf

        