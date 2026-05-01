


class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []
        return None

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -num)

        val_from_small = -heapq.heappop(self.small)
        heapq.heappush(self.big, val_from_small)

        if len(self.big) > len(self.small):
            val_from_big = heapq.heappop(self.big)
            heapq.heappush(self.small, -val_from_big)

        return None

    def findMedian(self) -> float:
        if len(self.small) != len(self.big):
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0]) / 2
        