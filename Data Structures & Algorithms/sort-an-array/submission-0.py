class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            inserted = False
            for i in range(len(arr)):
                if num < arr[i]:
                    arr.insert(i,num)
                    inserted =True
                    break
            if not inserted:
                arr.append(num)
        
        return arr
        