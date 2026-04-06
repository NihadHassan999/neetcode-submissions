'''
-> build graph and indegree array
-> initialise queue with courses without prerequisites
-> process courses in topological order
'''

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph and indegree array
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # initialise queue and fill it with prerequisites with no courses
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # process courses in topological order
        course_taken = 0

        while queue:
            course = queue.popleft()
            course_taken += 1

            # reduce indegree for neighbours 
            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return numCourses == course_taken