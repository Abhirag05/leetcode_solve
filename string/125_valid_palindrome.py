class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str=""
        for i in s.lower():
            if i.isalnum():
                new_str+=i
        return new_str==new_str[::-1]