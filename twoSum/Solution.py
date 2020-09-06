class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            value = target - nums[i]
            if value in nums:
                next_ind = nums.index(value)
                if next_ind != i:
                    return [i, next_ind]
