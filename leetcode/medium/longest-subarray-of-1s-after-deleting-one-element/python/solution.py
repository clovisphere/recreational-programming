from typing import List


def longest_subarray(nums: List[int]) -> int:
    result = start = zeros = 0
    for i in range(len(nums)):
        zeros += (j := 1 if nums[i] == 0 else 0)
        while zeros > 1:
            zeros -= (k := 1 if nums[start] == 0 else 0)
            start += 1
        result = max(result, i - start)
    return result


# let's test your implementation
assert longest_subarray([1,1,1]) == 2
#assert longest_subarray([1, 1, 0, 1]) == 3
#assert longest_subarray([0,1,1,1,0,1,1,0,1]) == 5
#assert longest_subarray([1,0,1,1,1,1,1,1,0,1,1,1,1,1]) == 11
