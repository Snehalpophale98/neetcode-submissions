class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        tuple_one = sorted_nums[0]*sorted_nums[1]
        tuple_two = sorted_nums[-1]*sorted_nums[-2]
        max_diff = tuple_two - tuple_one
        return max_diff
        