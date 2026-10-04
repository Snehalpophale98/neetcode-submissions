class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_from_right = -1
        for i in range(len(arr)-1,-1,-1):
            cur_elt = arr[i]
            arr[i] = max_from_right
            if cur_elt > max_from_right:
                max_from_right = cur_elt
        return arr



        