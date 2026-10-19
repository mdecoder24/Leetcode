class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = [i for i, v in enumerate(nums) if v == target]

        return result