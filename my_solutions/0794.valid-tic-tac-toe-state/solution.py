class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(x):
            # TODO: implement
            pass
        x = sum(board[i][j] == 'X' for i in range(3) for j in range(3))
