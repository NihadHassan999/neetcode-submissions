'''
-> initialise parentheses hashmap and stack
-> traverse the input string
-> if c is opening bracket, push to stack, need to find closing later
-> if c is closing bracket (i.e, it is in map) we check stack empty check and top of stack check
-> if not, pop from stack
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in Map:
                stack.append(c)
                continue

            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack
        