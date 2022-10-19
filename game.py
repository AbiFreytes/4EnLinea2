from exception import NoSpace, NoValidNumber


class Rules:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.board = [[' ' for x in range(self.cols)] for i in range(self.rows)]
        self.player1 = ''
        self.player2 = ''
        self.turn = 1
        self.winner = ''

    def players(self, marker1, marker2):
        self.player1 = marker1
        self.player2 = marker2
        return self.player1, self.player2

    def space_check(self, col):
        i = len(self.board) - 1
        while i >= 0:
            if self.board[i][col] == ' ':
                return i
            i -= 1
        return -1

    def insert_marker(self, col):
        if not 7 >= col >= 0:
            raise NoValidNumber
        fila = self.space_check(col)
        if fila == -1:
            raise NoSpace
        if self.turn == 1:
            self.board[fila][col] = self.player1
            self.turn += 1
        elif self.turn == 2:
            self.board[fila][col] = self.player2
            self.turn -= 1
        return True

    def verify_col(self):
        for x in range(5):
            for y in range(8):
                if self.board[x][y] == self.player1 and self.board[x+1][y] == self.player1 and self.board[x+2][y] == self.player1 and self.board[x+3][y] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[x][y] == self.player2 and self.board[x+1][y] == self.player2 and self.board[x+2][y] == self.player2 and self.board[x+3][y] == self.player2:
                    self.winner = 'Jugador 2'
                    return True

    def verify_row(self):
        for x in range(8):
            for y in range(5):
                if self.board[x][y] == self.player1 and self.board[x][y+1] == self.player1 and self.board[x][y+2] == self.player1 and self.board[x][y+3] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[x][y] == self.player2 and self.board[x][y+1] == self.player2 and self.board[x][y+2] == self.player2 and self.board[x][y+3] == self.player2:
                    self.winner = 'Jugador 2'
                    return True

    def verify_diag_up_right_to_left(self):
        for x in range(5):
            for y in range(5):
                if self.board[x][y] == self.player1 and self.board[x+1][y+1] == self.player1 and self.board[x+2][y+2] == self.player1 and self.board[x+3][y+3] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[x][y] == self.player2 and self.board[x+1][y+1] == self.player2 and self.board[x+2][y+2] == self.player2 and self.board[x+3][y+3] == self.player2:
                    self.winner = 'Jugador 2'
                    return True

    def verify_diag_up_left_to_right(self):
        for x in range(5):
            for y in range(3, 8):
                if self.board[x][y] == self.player1 and self.board[x+1][y-1] == self.player1 and self.board[x+2][y-2] == self.player1 and self.board[x+3][y-3] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[x][y] == self.player2 and self.board[x+1][y-1] == self.player2 and self.board[x+2][y-2] == self.player2 and self.board[x+3][y-3] == self.player2:
                    self.winner = 'Jugador 2'
                    return True

    def check_winner(self):
        if self.verify_diag_up_left_to_right() == True:
            return True
        elif self.verify_diag_up_right_to_left() == True:
            return True
        elif self.verify_col() == True:
            return True
        elif self.verify_row() == True:
            return True
        else:
            return False
