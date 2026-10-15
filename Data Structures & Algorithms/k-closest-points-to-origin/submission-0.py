class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        for index, point in enumerate(points):
            x1 = 0
            y1 = 0
            x2 = point[0]
            y2 = point[1]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            points[index] = tuple([dist, [x2, y2]])

        maxheap = points
        heapq.heapify_max(maxheap)
        while len(maxheap) > k:
            heapq.heappop_max(maxheap)

        res = [n[1] for n in maxheap]

        return res