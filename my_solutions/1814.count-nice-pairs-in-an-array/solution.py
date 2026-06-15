class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            # TODO: implement
            pass
        cnt = Counter(x - rev(x) for x in nums)
