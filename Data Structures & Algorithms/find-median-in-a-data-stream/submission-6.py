


class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0
        return None

    def addNum(self, num: int) -> None:
        if self.size > 0:
            for i in range(self.size):
                if num < self.arr[i]:
                    self.arr.insert(i, num)
                    break
            else:
                self.arr.append(num)
        else:
            self.arr.append(num)
        self.size += 1
        print(self.arr)
        return None

    def findMedian(self) -> float:
        mid = self.size // 2
        if self.size % 2 == 1:
            return float(self.arr[mid])
        else:
            return (self.arr[mid] + self.arr[mid-1]) / 2
        