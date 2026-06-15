class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def f(x):
            # TODO: implement
            pass
        return bisect_left(range(max(nums) + 1), True, key=f)
