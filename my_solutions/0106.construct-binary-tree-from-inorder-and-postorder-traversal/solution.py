class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            # TODO: implement
            pass
        d = {v: i for i, v in enumerate(inorder)}
