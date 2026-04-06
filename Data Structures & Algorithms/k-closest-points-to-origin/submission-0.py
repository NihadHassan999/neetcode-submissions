'''
-> create empty minheap, iterate through points and add distance, x, y to minHeap
-> heapify the minHeap
-> creaty empty res
-> while k>0, pop and append x, y to the res 
'''
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        
        return res
        