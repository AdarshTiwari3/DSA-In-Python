from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squareGrid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    squareGrid[(r // 3, c // 3)].add(num)

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            for num in '123456789':
                if num not in rows[r] and num not in cols[c] and num not in squareGrid[(r // 3, c // 3)]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    squareGrid[(r // 3, c // 3)].add(num)

                    if backtrack(r, c + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    squareGrid[(r // 3, c // 3)].remove(num)

            return False

        backtrack(0, 0)
