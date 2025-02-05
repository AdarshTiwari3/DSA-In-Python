class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen=len(board)
        colLen=len(board[0])
        print("colLen=",colLen)
        def helper(ind,row,col):
            if row>=rowLen or row<0 or col<0 or col>=colLen or board[row][col]!= word[ind]: #check for out of bound case , if it is return False
                return False

            if ind==len(word)-1: #found the entire word in board
                return True
            backTrackVariable=board[row][col]
            board[row][col]="*"
            result = helper(ind+1, row-1, col) or helper(ind+1, row, col-1) or helper(ind+1, row+1, col) or helper(ind+1, row, col+1)

            #backtrack
            board[row][col]=backTrackVariable
            return result


        # check the word[i] or starting letter in the board then do the backtracking logic

        for r in range(rowLen):
            for c in range(colLen):
                if board[r][c]==word[0]:
                    if helper(0,r,c):
                        return True
        return False