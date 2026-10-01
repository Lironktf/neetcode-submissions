import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        res = []

        for i, point in enumerate(points):
            nums.append(((math.sqrt((point[0] * point[0]) + (point[1] * point[1]))), i))
        
        print(nums)
        heapq.heapify(nums)
        print(nums)

        for i in range(k):
            dist, index = heapq.heappop(nums)
            res.append(points[index])

        return res
#sqrt26 sqrt20
