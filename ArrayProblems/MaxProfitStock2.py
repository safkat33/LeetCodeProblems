from typing import List



class Solution:
    def getProfit(self, arr):
        global_profit = 0
        buying_price = arr[0]
        selling_day = None
        for i in range(1, len(arr)):
            profit = 0
            selling_day = None
            if arr[i] <= buying_price:
                buying_price = arr[i]
            elif arr[i] - buying_price > profit:
                profit = (arr[i] - buying_price)
                selling_day = i
                while selling_day + 1 < len(arr) - 1:
                    profit_i, selling_day = self.getProfit(arr[selling_day + 1:])
                    profit += profit_i
                    if selling_day is not None:
                        selling_day += (i + 1)
                    else:
                        break
            global_profit = max(global_profit, profit)

        # print(global_profit)
        return global_profit, selling_day

    def maxProfit(self, prices: List[int]) -> int:
        profit, selling_day = self.getProfit(prices)
        return profit

    '''
    [7,1,5,3,6,4]

    [b-1,s-5,3,6,4]
    profit = 4
    [b-3,s-6,4]
    profit = 4+3 = 7

    [1,5,6,3,5]

    [b-1,s-5,6,3,5]
    profit = 4
    [6,b-3,s-4]
    profit = 4+1 = 5



    '''