class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
            
                