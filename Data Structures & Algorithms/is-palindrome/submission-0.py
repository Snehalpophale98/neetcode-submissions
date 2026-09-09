class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(cleaned)//2):
            if cleaned[i] != cleaned[len(cleaned)-i-1]:
                return False
        return True
        