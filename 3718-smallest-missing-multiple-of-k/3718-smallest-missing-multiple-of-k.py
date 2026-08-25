class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        nums_set = set(nums)
        x = k
        while x in nums_set:
            x += k
            
        return x