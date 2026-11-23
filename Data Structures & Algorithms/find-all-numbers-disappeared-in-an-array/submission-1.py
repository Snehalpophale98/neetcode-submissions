class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        output_no = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                output_no.append(i)
        return output_no



        