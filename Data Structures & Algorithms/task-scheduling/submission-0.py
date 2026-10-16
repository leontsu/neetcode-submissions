class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxheap = [-n for n in count.values()]
        heapq.heapify(maxheap)        

        q = deque([])

        time = 0
        while maxheap or q:
            time += 1
            if q and q[0][1] == time:
                qcount, qtime = q.popleft()
                heapq.heappush(maxheap, -qcount)

            if maxheap:
                count = -(heapq.heappop(maxheap))
                if count - 1 > 0:
                    q.append([count - 1, time + n + 1])

        return time