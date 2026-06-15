class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def check(target: int, k: int) -> bool:
            # TODO: implement
            pass
        return check(nums[0], k) or check(-nums[0], k)
