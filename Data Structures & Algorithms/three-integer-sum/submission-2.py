class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        mySet = set()
        sort = sorted(nums)
        for i, num in enumerate(sort):
            l = i + 1
            r = len(sort) - 1
            while l < r:
                if sort[l] + sort[r] == -num:
                    mySet.add(tuple([num, sort[l], sort[r]]))
                    l += 1
                elif sort[l] + sort[r] > -num:
                    r -= 1
                else:
                    l += 1

        return list(mySet)



