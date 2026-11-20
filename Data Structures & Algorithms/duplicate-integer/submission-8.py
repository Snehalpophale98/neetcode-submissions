class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_elements = sorted(nums)
        for i in range(len(sorted_elements)-1):
            if sorted_elements[i] == sorted_elements[i+1]:
                return True
        return False