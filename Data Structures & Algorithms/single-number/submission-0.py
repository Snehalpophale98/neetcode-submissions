class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen =  {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for num,count in seen.items():
            if count == 1:
                return num

        