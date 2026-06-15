class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(mx: int) -> bool:
            # TODO: implement
            pass
        return bisect_left(range(1, max(nums) + 1), True, key=check) + 1
