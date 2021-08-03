import inspect
import timeit
from typing import List
import sys


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Runtime: 84 ms, faster than 93.81% of Python3 online submissions for Median of Two Sorted Arrays.
            Memory Usage: 14.7 MB, less than 24.05% of Python3 online submissions for Median of Two Sorted Arrays."""
        nums3 = sorted(nums1 + nums2)
        len_ = len(nums3)
        median_idx = len_ // 2

        if len_ % 2 == 0:
            return (nums3[median_idx - 1] + nums3[median_idx]) / 2

        return nums3[median_idx]


# Test Case
nums1 = [1, 2, 3, 4, 5, 12, 4, 24, 42, 41]
nums2 = [3, 5, 7, 1, 2, 5]

# timeit params
timeit_repeat = 1
timeit_numbers = 100


if __name__ == '__main__':
    solutions = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for _, solution in solutions:
        if _.startswith("Solution"):
            result = solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)
            t = timeit.Timer(
                lambda: solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)
            ).repeat(timeit_repeat, timeit_numbers)
            print(result, t)
