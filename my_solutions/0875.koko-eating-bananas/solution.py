class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int) -> bool:
            # TODO: implement
            pass
        return 1 + bisect_left(range(1, max(piles) + 1), True, key=check)
