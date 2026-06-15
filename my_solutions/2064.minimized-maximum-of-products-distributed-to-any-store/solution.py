class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(x):
            # TODO: implement
            pass
        return 1 + bisect_left(range(1, 10**6), True, key=check)
