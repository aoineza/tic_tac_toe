'Tic-Tac-Toe Mechanics'

import copy

class game_board():
    def __init__(self):
        self.board = [['','',''],['','',''],['','','']]
    
    def add_element(self,element,row,column):
        if self.board[row][column] != '':
            return False
        self.board[row][column] = element
        return True
        
    def hor_match(self):
        for i,row in enumerate(self.board,0):
            if row == ['X','X','X'] or row == ['O','O','O']:
                return (True,i)
        return (False,0)
        
    def transpose(self):
        t_board = [['','',''],['','',''],['','','']]
        for i in range(3):
            for j in range(3):
                t_board[i][j] = self.board[j][i]
        return t_board
    
    def vert_match(self):
        t_board = self.transpose()
        record = copy.copy(self.board)
        self.board = t_board
        res = self.hor_match()
        self.board = record
        return res 
    
    def diag_match(self):
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != '':
            return (True,'left')
        elif self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1] and self.board[0][2] != '':
            return (True,'right')
        else:
            return (False,0)
        
