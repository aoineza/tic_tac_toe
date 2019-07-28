'Board Unit Tests'

import unittest
from mechanics import game_board

class TestBoardMatchees(unittest.TestCase):
    
    
    def test_hor_match(self):
        board1 = game_board()
        board1.board = [['X','O','X'],['','',''],['X','X','X']]
        board2 = game_board()
        board2.board = [['X','X','O'],['','',''],['','','O']]
        self.assertTrue(board1.hor_match()[0])
        self.assertFalse(board2.hor_match()[0])
    
    def test_vert_match(self):
        board3 = game_board()
        board3.board = [['X','','O'],['X','',''],['','','O']]
        board4 = game_board()
        board4.board = [['X','',''],['X','',''],['X','','']]
        self.assertFalse(board3.vert_match()[0])
        self.assertTrue(board4.vert_match()[0])
    
    def test_diag_match(self):
        board4 = game_board()
        board4.board = [['X','',''],['','',''],['','','X']]
        board5 = game_board()
        board5.board = [['','','O'],['','O',''],['O','','']]
        board6 = game_board()
        board6.board = [['X','',''],['','X',''],['','','X']]
        self.assertFalse(board4.diag_match()[0])
        self.assertTrue(board5.diag_match()[0])
        self.assertTrue(board6.diag_match()[0])
    
    def test_insert_element(self):
        board7 = game_board()
        board7.add_element('X',0,2)
        self.assertEqual(board7.board,[['','','X'],['','',''],['','','']])   
if __name__ == '__main__':
    unittest.main()
    
                
