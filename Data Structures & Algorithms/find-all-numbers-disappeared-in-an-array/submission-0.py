class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        list1 = []
        n = len(nums)
        for i in range(1,n+1):
            if i not in nums:
                list1.append(i)
        return list1


        