class Solution:
    def numWays(self, s: str) -> int:
        def find(x):
            # TODO: implement
            pass
        cnt, m = divmod(sum(c == '1' for c in s), 3)
