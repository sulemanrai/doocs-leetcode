class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            # TODO: implement
            pass
        return bisect_left(range(len(nums)), True, key=f)
