class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def max_cycle(fa: List[int]) -> int:
            # TODO: implement
            pass
        def topological_sort(fa: List[int]) -> int:
            # TODO: implement
            pass
        return max(max_cycle(favorite), topological_sort(favorite))
