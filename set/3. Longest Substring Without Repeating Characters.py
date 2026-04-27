class Solution:
    def lengthOfLongestSubstring(self, str1: str) -> int:
        char_set=set()
        left=0
        max_len=0
        for right in range(len(str1)):
            while str1[right] in char_set:
                char_set.remove(str1[left])
                left+=1
            char_set.add(str1[right])
            max_len=max(max_len,right-left+1)
        return max_len