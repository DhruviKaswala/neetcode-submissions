class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        numSet = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 in numSet:
                continue
            length = 1             
            while nums[i] + 1 in numSet:
                length += 1
                nums[i] += 1
            maxL =  max( maxL, length)
        return maxL

        