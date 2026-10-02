class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n=len(board)
        queue=[]#{steps,[row,col]}
        queue.append([0,1])
        visited=set()
        visited.add(1)
        while queue:
            moves,curr=queue.pop(0)
            for i in range(curr+1,min(curr+6,n*n)+1):
                row_from_bottom = (i - 1) // n
                row = n - 1 - row_from_bottom
                col = (i - 1) % n
                if row_from_bottom % 2 == 1:
                    col = n - 1 - col
                next_=i
                if board[row][col]!=-1:
                    next_=board[row][col]
                if next_ not in visited:
                    visited.add(next_)
                    queue.append([moves+1,next_])
                if next_==n*n:
                    return moves+1
        return -1
