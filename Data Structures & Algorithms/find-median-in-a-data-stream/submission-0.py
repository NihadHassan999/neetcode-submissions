'''
def init: 
    -> two heaps : small and large
def addNum:
    -> initial check if num is larger than smallest number in large
    -> push logic after intial check
    -> rebalance small or rebalance large
def findMedian:
    -> if unequal sizes, if small has more, its there, if large vice versa
    -> if equal, get mean
    -
'''

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
        
        
        