class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def lis(arr):
            # TODO: implement
            pass
        return sum(lis(arr[i::k]) for i in range(k))
