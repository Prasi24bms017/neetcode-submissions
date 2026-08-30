from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_list=sorted(nums)
      
        heap=[]
        for i in sorted_list:
            heappush(heap,i)
            if len(heap)>k:
                heappop(heap)
        return heap[0]
        
        