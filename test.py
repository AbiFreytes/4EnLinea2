import unittest
from game import Rules


class TestGame(unittest.TestCase):
    def test_board(self):
        game = Rules()
        self.assertEqual(len(game.board), 8)
        self.assertEqual(len(game.board[0]), 8)
        self.assertEqual(len(game.board[1]), 8)
        self.assertEqual(len(game.board[2]), 8)
        self.assertEqual(len(game.board[3]), 8)
        self.assertEqual(len(game.board[4]), 8)
        self.assertEqual(len(game.board[5]), 8)
        self.assertEqual(len(game.board[6]), 8)
        self.assertEqual(len(game.board[7]), 8)

    def test_players(self):
        game = Rules()
        game.players('m', 'a')
        self.assertEqual(game.player1, 'm')
        self.assertEqual(game.player2, 'a')

    def test_space(self):
        game = Rules()
        self.assertTrue(game.space_check(5))

    def test_marker(self):
        game = Rules()
        game.player1 = 'X'
        game.player2 = 'y'
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        self.assertEqual(game.board, [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                    ['X', ' ', 'y', ' ', ' ', ' ', ' ', ' '],
                                    ['X', ' ', 'y', ' ', ' ', ' ', ' ', ' '],
                                    ['X', ' ', 'y', ' ', ' ', ' ', ' ', ' ']])

    def test_winner_col(self):
        game = Rules()
        game.player1 = 'X'
        game.player2 = 'y'
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        self.assertEqual(game.verify_col(), True)
        self.assertEqual(game.winner, 'Jugador 1')

    def test_winner_row(self):
        game = Rules()
        game.player1 = 'X'
        game.player2 = 'y'
        game.insert_marker(0)
        game.insert_marker(0)
        game.insert_marker(1)
        game.insert_marker(0)
        game.insert_marker(2)
        game.insert_marker(0)
        game.insert_marker(3)
        self.assertEqual(game.verify_row(), True)
        self.assertEqual(game.winner, 'Jugador 1')

    def test_diag_left(self):
        game = Rules()
        game.player1 = 'X'
        game.player2 = 'y'
        game.insert_marker(0)
        game.insert_marker(1)
        game.insert_marker(1)
        game.insert_marker(2)
        game.insert_marker(2)
        game.insert_marker(3)
        game.insert_marker(2)
        game.insert_marker(3)
        game.insert_marker(3)
        game.insert_marker(7)
        game.insert_marker(3)
        self.assertEqual(game.verify_diag_up_left_to_right(), True)

    def test_diag_right(self):
        game = Rules()
        game.player1 = 'X'
        game.player2 = 'y'
        game.insert_marker(3)
        game.insert_marker(2)
        game.insert_marker(2)
        game.insert_marker(1)
        game.insert_marker(1)
        game.insert_marker(0)
        game.insert_marker(1)
        game.insert_marker(0)
        game.insert_marker(0)
        game.insert_marker(7)
        game.insert_marker(0)
        print(game.board)
        self.assertEqual(game.verify_diag_up_right_to_left(), True)


if __name__ == '__main__':
    unittest.main()
