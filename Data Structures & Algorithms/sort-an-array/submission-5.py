class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.heapSort(nums, len(nums))
        return nums


    def heapify(self, arr, n, i):

        l = (i << 1) + 1
        r = (i << 1) + 2
        largestNum = i

        if l < n and arr[l] > arr[largestNum]:
            largestNum = l
        
        if r < n and arr[r] > arr[largestNum]:
            largestNum = r

        if largestNum != i:
            arr[i], arr[largestNum] = arr[largestNum], arr[i]
            self.heapify(arr, n, largestNum)


    def heapSort(self, arr, n):
        
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
