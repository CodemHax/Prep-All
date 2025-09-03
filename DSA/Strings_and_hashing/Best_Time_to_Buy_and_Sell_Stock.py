class Solution:
    @staticmethod
    def maxProfit(prices):
        if prices is None:
            return 0
        max_profit = 0
        low_buy = prices[0]
        for price in prices:
            low_buy = min(low_buy , price)
            profit = price - low_buy
            max_profit = max(max_profit , profit)
        return max_profit


if __name__ == '__main__':
    maxProfit = Solution.maxProfit([1 , 2])
    print(maxProfit)



