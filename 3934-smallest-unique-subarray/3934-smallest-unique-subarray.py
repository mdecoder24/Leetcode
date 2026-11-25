from typing import Dict, List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        base = 19
        modulo = 10**9 + 7
        powers = [1] * (n + 1)
        for idx in range(1, n + 1):
            powers[idx] = (powers[idx - 1] * base) % modulo
        for window_len in range(1, n + 1):
            if self._has_unique_window(nums, window_len, base, modulo, powers):
                return window_len

        return n  

    def _has_unique_window(
        self,
        nums: List[int],
        window_len: int,
        base: int,
        modulo: int,
        powers: List[int],
    ) -> bool:
        n = len(nums)
        hash_counts: Dict[int, int] = {}
        current_hash = 0
        for idx in range(window_len):
            current_hash = (current_hash * base + nums[idx]) % modulo
        hash_counts[current_hash] = 1
        for idx in range(1, n - window_len + 1):
            leftmost_contribution = (powers[window_len - 1] * nums[idx - 1]) % modulo
            current_hash = (current_hash - leftmost_contribution) % modulo
            current_hash = (current_hash * base + nums[idx + window_len - 1]) % modulo

            hash_counts[current_hash] = hash_counts.get(current_hash, 0) + 1
        return 1 in hash_counts.values()

from typing import Dict, List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        self.nums = nums
        self.base = 19
        self.modulo = 10**9 + 7
        self.powers = [1] * (len(nums) + 1)
        for idx in range(1, len(nums) + 1):
            self.powers[idx] = (self.powers[idx - 1] * self.base) % self.modulo

        self.hash_values: Dict[int, int] = {}

        min_possible_len = len(nums)         
        min_len, max_len = 1, len(nums)        
        while min_len <= max_len:
            mid_len = (min_len + max_len) // 2

            if self._check_uniqueness(mid_len):
                min_possible_len = min(min_possible_len, mid_len)
                max_len = mid_len - 1
            else:
                min_len = mid_len + 1

        return min_possible_len

    def _check_uniqueness(self, subarray_len: int) -> bool:
        current_hash = 0
        for idx in range(subarray_len):
            current_hash = (current_hash * self.base + self.nums[idx]) % self.modulo

        self.hash_values.clear()
        self.hash_values[current_hash] = 1
        for idx in range(1, len(self.nums) - subarray_len + 1):
            leftmost = (self.powers[subarray_len - 1] * self.nums[idx - 1]) % self.modulo
            current_hash = (current_hash - leftmost) % self.modulo
            current_hash = (current_hash * self.base + self.nums[idx + subarray_len - 1]) % self.modulo

            self.hash_values[current_hash] = self.hash_values.get(current_hash, 0) + 1
        return 1 in self.hash_values.values()
