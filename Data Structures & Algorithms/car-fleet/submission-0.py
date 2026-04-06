'''
-> create zip pairs from position and speed
-> reverse the created zip pairs
-> iterate, append time taken to stack
-> if current time <= previous time at [-1], pop
-> finally return length of stack
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            # time taken = diff in distance / speed
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack) 