# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         cur = 0 
#         # for this problem we know that the character is not important but the number of different charracters
#         # we can use built in function in python Counter() to reture a map with element : amount in it
#         tasks = Counter(tasks)
#         # we don't need to know which character, only how many characters so we need only the value 
#         amount = [-i for i in tasks.values()]
#         heapq.heapify(amount)
#         # each time we process a task, we pop the most frequent value and after process it we push it to the heap again
#         # we use queue to store all pull out task until they meet the time requirement
#         waitTask = deque()
#         while amount or waitTask:
#             cur += 1
#             if amount:
#                 currtask = heapq.heappop(amount)
#             else:
#                 task = waitTask.popleft()
#                 currtask = task[1]
#                 cur  = task[0] + 1
#             if currtask + 1 != 0:
#                 waitTask.append([cur + n ,currtask + 1])
#             # add the tasks back to amount 
#             if waitTask and waitTask[0][0] == cur:
#                 heapq.heappush(amount,waitTask.popleft()[1])
#             # currtask + 1 != 0 means these task not finished
#             print(currtask,cur)
            
#         return cur
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time