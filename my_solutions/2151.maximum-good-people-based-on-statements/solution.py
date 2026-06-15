class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        def check(mask: int) -> int:
            # TODO: implement
            pass
        return max(check(i) for i in range(1, 1 << len(statements)))
