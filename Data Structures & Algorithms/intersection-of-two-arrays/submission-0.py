class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = []
        for num in nums1:
            if num in nums2 and num not in list1:
                list1.append(num)
        return list1

        