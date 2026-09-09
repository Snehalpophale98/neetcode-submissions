class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count_dict = {}
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        lucky_int = -1
        for key,value in count_dict.items():
            if key == value:
                lucky_int = max(lucky_int,key)
        return lucky_int
        