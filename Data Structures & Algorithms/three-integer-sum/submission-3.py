class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        sort = sorted(nums)
        for i, num in enumerate(sort):
            if i > 0 and num == sort[i -1]:
                continue
            
            l = i + 1
            r = len(sort) - 1
            while l < r:

                current_sum = sort[l] + sort[r] 
                if current_sum == -num:
                    output.append([num, sort[l], sort[r]])
                    l += 1
                    while l < r and sort[l] == sort[l - 1]:
                        l += 1
                elif current_sum > -num:
                    r -= 1
                else:
                    l += 1

        return output



