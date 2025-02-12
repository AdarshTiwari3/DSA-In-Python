class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        # optimise the isSafe check to use hash of row , left upper diagonal and left lower diagonal 
        #1. left upper diagonal- (row-col)
        #2. left lower diagonal- (row+col)
        rowCheck=set()
        leftUpperDiag=set()
        leftLowerDiag=set()
       
        def helper(col,board,rowCheck,leftUpperDiag,leftLowerDiag):
            if col==n:
                ans.append([''.join(row) for row in board])
                return 
            
            for row in range(n):
                # check if placing the queen is not safe
                if row in rowCheck or row-col in leftUpperDiag or row+col in leftLowerDiag:
                    continue
                    #maintain the set by marking the element
                else:
                    rowCheck.add(row)
                    leftUpperDiag.add(row-col)
                    leftLowerDiag.add(row+col)
                    board[row][col]='Q'
                    helper(col+1,board,rowCheck,leftUpperDiag,leftLowerDiag)
                    #backtrack
                    board[row][col]='.'
                    rowCheck.remove(row)
                    leftUpperDiag.remove(row-col)
                    leftLowerDiag.remove(row+col)

        board=[['.' for _ in range(n)] for _ in range(n)] #empty board with '.'
        # print("Board=",board)
        helper(0,board,rowCheck,leftUpperDiag,leftLowerDiag)
        return ans