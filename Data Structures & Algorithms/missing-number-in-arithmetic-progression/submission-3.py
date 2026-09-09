class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[-1]-arr[0])//n
        if d == 0:
            return arr[0]
        for i in range(n-1):
            if arr[i+1] - arr[i] != d :
                return arr[i] + d

        return -1