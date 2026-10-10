class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []
        for num in arr2:
            result.extend([num]*count[num])
            count[num] = 0
        for num in sorted(count):
            if count[num] > 0:
                result.extend([num]*count[num])
        return result