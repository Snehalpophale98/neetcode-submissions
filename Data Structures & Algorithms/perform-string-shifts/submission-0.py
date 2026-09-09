class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            for i in range(amount):
                if direction == 0:
                    s = s[1:] + s[0]
                else:
                    s = s[-1] + s[:-1]

        return s