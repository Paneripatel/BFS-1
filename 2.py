'''
Problem 2

Course Schedule (https://leetcode.com/problems/course-schedule/)
'''

from queue import Queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: # type: ignore
        if numCourses == 0:
            return True

        q = Queue()

        indegrees = [0 for i in range(numCourses)]
        Map = dict()
        count = 0
        for i in range(len(prerequisites)):
            From = prerequisites[i][1] #independent
            To = prerequisites[i][0] #dependent
            indegrees[To] = indegrees[To]+1
            if From not in Map:
                Map[From] = []
            Map[From].append(To)

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.put(i)
                count += 1

        if count == 0: #not able to add anything to q
            return False

        while q.qsize()  > 0:
            curr = q.get()
            if curr in Map:
                edges = Map[curr]
                for edge in edges:
                    indegrees[edge] -= 1
                    if indegrees[edge] == 0:
                        q.put(edge)
                        count += 1

        return count == numCourses                


