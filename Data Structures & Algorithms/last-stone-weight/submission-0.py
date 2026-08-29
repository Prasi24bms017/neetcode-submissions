from heapq import heappush ,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for wt in stones:
            heappush(heap,-wt)
        while len(heap)>1:
            y=-heappop(heap)
            x=-heappop(heap)
            if y!=x:
                heappush(heap,-(y-x))
        if heap:
            return -heap[0]
        return 0
        

        