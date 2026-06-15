class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g: List[List[int]]) -> bool:
            # TODO: implement
            pass
        return check(grid) or check(list(zip(*grid)))
