'''
-> Frequency Counting
-> maxHeap to track frequent tasks
-> time and queue simulation
-> execution loop
-> edge case for empty heap
'''
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        