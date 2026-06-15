class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(mx: int) -> bool:
            # TODO: implement
            pass
        return bisect_left(range(10**11), True, key=check)
