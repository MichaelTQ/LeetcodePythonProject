import heapq


class Solution:
    def kClosest(self, points, K):
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            if i >= j: return
            mid = partition(i, j)
            if K < mid-i+1:
                sort(i, mid-1, K)
            elif K > mid-i+1:
                sort(mid+1, j, K-(mid-i+1))

        def partition(i, j):
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points)-1, K)
        return points[:K]

    def kClosest_heap(self, points, K):
        heap = []
        for p in points:
            heapq.heappush(heap, (p[0]**2 + p[1]**2, p))
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
        return res
