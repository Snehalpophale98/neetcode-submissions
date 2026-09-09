class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        
        if target in count and count[target] > n //2:
            return True

        return False
             