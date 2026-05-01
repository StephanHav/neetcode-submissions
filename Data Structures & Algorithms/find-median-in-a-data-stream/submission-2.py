class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = len(self.arr)
        return None

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.size += 1
        return None

    def findMedian(self) -> float:
        mid = self.size // 2
        sort_arr = sorted(self.arr)
        if self.size % 2 == 1:
            return float(sort_arr[mid])
        else:
            return (sort_arr[mid] + sort_arr[mid-1]) / 2
        