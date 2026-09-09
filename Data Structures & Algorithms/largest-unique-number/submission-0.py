class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count_dict = {}
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        max_unique = -1
        for key,value in count_dict.items():
            if value == 1:
                max_unique = max(max_unique, key)
        return max_unique
                

        
        