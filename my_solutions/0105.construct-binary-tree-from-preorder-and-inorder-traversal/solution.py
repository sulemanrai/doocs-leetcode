class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(i: int, j: int, n: int) -> Optional[TreeNode]:
            # TODO: implement
            pass
        d = {v: i for i, v in enumerate(inorder)}
