class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for elem in range(1, len(nums)):
            nums[elem] += nums[elem - 1]

        return nums  