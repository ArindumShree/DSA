class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in box[(i//3)*3+(j//3)]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3)*3+(j//3)].add(board[i][j])
        return True