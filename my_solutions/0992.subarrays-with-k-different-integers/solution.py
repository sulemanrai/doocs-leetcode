class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            # TODO: implement
            pass
        return sum(a - b for a, b in zip(f(k - 1), f(k)))
