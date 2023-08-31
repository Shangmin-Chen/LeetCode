class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checking(board):
            for i in range(9):
                for j in range(9):
                    num = j+1
                    if board[i].count(str(num)) > 1:
                        return False
            return True
        def divide_cells(r1,r2,cells,board):
            i = 0
            empty = []
            while i<9:
                empty = empty + board[i][r1:r2] 
                if len(empty) == 9:
                    cells.append(empty)
                    empty = []
                i+=1

        columns = [[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                columns[i].append(board[j][i])

        cells = []
        divide_cells(0,3,cells,board)
        divide_cells(3,6,cells,board)
        divide_cells(6,9,cells,board)


    
        return checking(board) and checking(columns) and checking(cells)
                