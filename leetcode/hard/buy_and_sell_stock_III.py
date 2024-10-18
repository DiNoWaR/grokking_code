"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List


class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        if not prices:
            return 0

            # Инициализация переменных для максимальной прибыли
        first_buy = float('-inf')  # Прибыль после первой покупки
        first_sell = 0  # Прибыль после первой продажи
        second_buy = float('-inf')  # Прибыль после второй покупки
        second_sell = 0  # Прибыль после второй продажи

        for price in prices:
            # Обновляем прибыль после первой покупки (стремимся минимизировать потери)
            first_buy = max(first_buy, -price)
            # Обновляем прибыль после первой продажи
            first_sell = max(first_sell, first_buy + price)
            # Обновляем прибыль после второй покупки (учитывая прибыль от первой продажи)
            second_buy = max(second_buy, first_sell - price)
            # Обновляем прибыль после второй продажи
            second_sell = max(second_sell, second_buy + price)

        return second_sell

sol = Solution()
print(sol.max_profit([3,3,5,0,0,3,1,4]))
print(sol.max_profit([1,2,3,4,5]))
print(sol.max_profit([7,6,4,3,1]))