#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#

from sys import  maxint

class Solution(object):
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 1
        maxProfit = 0
        l = len(prices)
        while i < l:
            if i == -l:
                break
            j = 1
            while j < l:
                if i + j > l:
                    break
                profit = prices[-i] - prices[-i-j]
                if profit > 0 and profit > maxProfit:
                    maxProfit = profit
                j += 1
            i += 1
        return maxProfit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = maxint
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit

if  __name__ ==  '__main__':
    solution = Solution()
    inputArr = [7, 1, 5, 3, 6, 4]
    print('Input: ', inputArr)
    print('Out: ',solution.maxProfit(inputArr))
    inputArr = [7,6,4,3,1]
    print('Input: ', inputArr)
    print('Out: ', solution.maxProfit(inputArr))