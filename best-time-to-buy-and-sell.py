class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ls=[0]*len(prices)
        for i in range(1,len(ls)):
            if prices[i-1] >= prices[i]:
                ls[i]=ls[i-1]
            elif prices[i-1] < prices[i]:
                ls[i]=ls[i-1]+prices[i]-prices[i-1]
        return ls[-1]
            

