class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = {i:[] for i in range(numCourses)} 
        
        for course, pre in prerequisites:
            coursemap[course].append(pre)
        visiting = set()
        def dfs(coursenum):
            if coursenum in visiting:
                return False
            if coursenum not in coursemap.keys():
                return True
            visiting.add(coursenum)
            for i in coursemap[coursenum]:
                if not dfs(i):
                    return False
                coursemap[coursenum].remove(i)
            visiting.remove(coursenum)
            return True
        for j in range(numCourses):
            if not dfs(j):
                return False
        return True