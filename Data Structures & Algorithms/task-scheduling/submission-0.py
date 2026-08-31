from collections import Counter
from heapq import heappush , heappop
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[]
        for freq in count.values():
            heappush(heap,-freq)
        queue=deque()
        time=0
        while heap or queue:
            time +=1
            if queue and queue[0][0] <= time:
                ready_task = queue.popleft()
                heappush(heap, -ready_task[1])
            if heap: 
                freq=-heappop(heap)
                freq-=1
                if freq > 0:
                    queue.append((time + n+1, freq))
        return time

        