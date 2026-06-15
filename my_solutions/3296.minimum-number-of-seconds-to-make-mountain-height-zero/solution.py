class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(t: int) -> bool:
            # TODO: implement
            pass
        return bisect_left(range(10**16), True, key=check)
