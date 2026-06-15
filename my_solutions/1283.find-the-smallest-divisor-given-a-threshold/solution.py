class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def f(v: int) -> bool:
            # TODO: implement
            pass
        return bisect_left(range(max(nums)), True, key=f) + 1
