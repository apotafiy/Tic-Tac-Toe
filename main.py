class TTT:

    def __init__(self):
        self.board = []
        for i in range(0, 9):
            self.board.insert(i, i + 1)
        self.game()

    def display(self):
        print(f'{self.board[6]}|{self.board[7]}|{self.board[8]}')
        print('-----')
        print(f'{self.board[3]}|{self.board[4]}|{self.board[5]}')
        print('-----')
        print(f'{self.board[0]}|{self.board[1]}|{self.board[2]}')

    def check(self):
        """checks if there is a winner"""
        for i in range(2, 9, 3):
            if self.board[i] == self.board[i - 1] == self.board[i - 2]:
                return True

        for i in range(0, 3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6]:
                return True

        if self.board[0] == self.board[4] == self.board[8] or self.board[2] == self.board[4] == self.board[6]:
            return True
        else:
            return False

    def full(self):
        """checks if board is full, which means there is a tie"""
        x = 0
        for i in self.board:
            if not ((i == 'X') or (i == 'O')):
                x += 1
        if x == 0:
            return True
        else:
            return False

    def game(self):
        player = 'X'
        while not self.check():
            if self.full():
                self.display()
                print('TIE GAME')
                return
            self.display()
            move = int(input(f'Player {player}, Enter your move. 1-9\n'))
            while self.board[move - 1] == 'X' or self.board[move - 1] == 'O':
                move = int(input('That spot is already taken. Choose another.'))
            self.board[move - 1] = player
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        self.display()
        if player == 'X':
            print('Player O is the Winner')
        else:
            print('Player X is the Winner')


if __name__ == '__main__':
    TicTacToe = TTT()
