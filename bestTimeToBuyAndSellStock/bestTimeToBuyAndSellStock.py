class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxPrice = -1
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
                maxPrice = -1
            if price > maxPrice:
                maxPrice = price
            if maxPrice - minPrice > maxProfit:
                maxProfit = maxPrice - minPrice

        return maxProfit
            
