class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(t: int) -> bool:
            # TODO: implement
            pass
        return bisect_left(range(ranks[0] * cars * cars), True, key=check)
