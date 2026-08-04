class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        ans=right
        while left<=right:
            k=(left+right)//2
            hours=self.calc_hours(piles,k)
            if hours<=h:
                ans=k
                right=k-1
            else:
                left=k+1
        return ans
    def calc_hours(self,piles,k):
        total=0
        for  pile in piles:
            total+=math.ceil(pile/k)
        return total

