'''
-> piles=[3,6,7,11]; h=8; ban-per-h=[1,2,3,4,5,6,7,8,9,10,11]
-> use 2 pointers
-> find the time taken = summation of (pile / eating rate)
-> keep settings min k
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r # eating rate will be atleast max k in worst case scenario
        
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res