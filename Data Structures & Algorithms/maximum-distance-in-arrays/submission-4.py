class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        glob_max = arrays[0][-1]
        glob_min = arrays[0][0]
        max_dist = 0
        for i in range(1,len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            max_dist = max(max_dist,abs(current_max - glob_min))
            max_dist = max(max_dist,abs(glob_max - current_min))

            glob_max = max(current_max,glob_max)
            glob_min = min(current_min,glob_min)
            
        return max_dist


        