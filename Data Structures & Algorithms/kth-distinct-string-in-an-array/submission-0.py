class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for string in arr:
            count[string] = count.get(string,0)+ 1
        distinct_count = 0
        for string in arr:
            if count[string] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return string
        return ""
    


