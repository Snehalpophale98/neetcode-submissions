class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = nums.copy()
        nums.extend(list1)
        return nums


        