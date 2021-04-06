import math

class Solution:
    def minOperations(self, n):

        arr = [2 * i + 1 for i in range(0, n)]

        target = sum(arr) / n

        min_opt = 0

        for i in range(0, n):
            diff = target - arr[i]
            if diff > 0:
                min_opt += diff
            else:
                break

        return min_opt




a = Solution()

print(a.minOperations(3))




