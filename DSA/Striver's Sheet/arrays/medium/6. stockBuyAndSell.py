"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your
profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:
    def maxProfitBF(self, prices: list[int]) -> int:
        """
        Brute force: for each ith element, calculate its profit from every other element
                    if profit > max profit, update the max profit
        :TC: O(N*N)
        :SC: O(1)
        :param prices:
        :return:
        """
        max_sum = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_sum = max(max_sum, prices[j] - prices[i])
        return max(0, max_sum)

    def maxProfitBT(self, prices: list[int]) -> int:
        """
        using inbuild funtion: for every ith element calculate the max element from i+1 to nth
                                element and compute profit for this max element and ith element
                                if profit > max_profit, update the max_profit
        :param prices:
        :return:
        """
        max_sum = 0
        for i in range(len(prices) - 1):
            # iterate over the whole array till n-1
            # ignored last element as it can only be bought and can't be sold

            max_sum = max(max_sum, max(prices[i + 1:]) - prices[i])
        return max(0, max_sum)

    def maxProfitOP(self, prices: list[int]) -> int:
        """
        Optimal approach: instead of calculating max element from the remaining array,
                        keep a track of min element till now. If item to be sold on ith index,
                        max profit will happen only when it was bought on min price till now
        :param prices:
        :return:
        """
        mini = prices[0] # initializing min price with first element of the array
        maxi = 0  # need only profits not loss.In worst case we would buy and sell on the same day to make  profit zero

        for i in prices:
            # iterating through complete array

            mini = min(mini, i)  # tracking min element till now
            maxi = max(maxi, i - mini)  # update maxi if i-mini is maximum

        return maxi


a = [7, 1, 5, 3, 6, 4]
obj = Solution()
print(obj.maxProfitBF(a))
print(obj.maxProfitBT(a))
print(obj.maxProfitOP(a))
