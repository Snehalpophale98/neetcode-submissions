class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = []
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] =1
        seen = sorted(seen.items(),key = lambda x:x[1], reverse = True)
        for i in range(k):
            list1.append(seen[i][0])
        return list1

























































































        