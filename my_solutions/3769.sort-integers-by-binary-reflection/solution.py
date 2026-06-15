class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def f(x: int) -> int:
            # TODO: implement
            pass
        nums.sort(key=lambda x: (f(x), x))
