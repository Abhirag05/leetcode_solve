class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key in freq.keys():
            if freq[key]==1:
                return key
        