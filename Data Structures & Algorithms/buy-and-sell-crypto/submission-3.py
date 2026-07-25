class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp=prices[0]
        profit=0
        for sp in range(1,len(prices)):
            if prices[sp]<cp:
                cp=prices[sp]
            else: 
                current_profit=prices[sp]-cp
                profit=max(current_profit,profit)
        return profit 


        
        