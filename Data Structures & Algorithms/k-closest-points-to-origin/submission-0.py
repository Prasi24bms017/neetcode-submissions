from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        
        for point in points:
            x,y=point[0],point[1]
            
            distance=x*x+y*y
            heappush(heap,(-distance,point))
            if len(heap)>k:
                heappop(heap)
        result=[]
        for pair in heap:
            result.append(pair[1])            

        return result
        