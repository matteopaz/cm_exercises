from matrix import Matrix
import random


class Game:
    def __init__(self, player1, player2, x=6, y=7):
        self.board = Matrix(x, y, 0)
        self.player1 = player1
        self.player2 = player2
    
    def diags(self):
        b = self.board
        rows = b.get_dim()[0]
        cols = b.get_dim()[1]
        diags = []
        for i in range(cols + rows):
            diag = []
            for j in range(i):
                r = j
                c = i - j - 1
                if r >= rows or c >= cols or c < 0 or r < 0:
                    continue
                diag.append(b.get_el(r, c))
            diags.append(diag)
        return diags

    def __check_win(self):
        rows = self.board.get_raw()
        cols = self.board.transpose().get_raw()

        for i in range(len(rows[0]) - 3):
            for row in rows:
                if row[i:i+4] == [1, 1, 1, 1]:
                    return 1
                if row[i:i+4] == [2, 2, 2, 2]:
                    return 2
        for i in range(len(cols[0]) - 3):
            for col in cols:
                if col[i:i+4] == [1, 1, 1, 1]:
                    return 1
                if col[i:i+4] == [2, 2, 2, 2]:
                    return 2
        diags = self.diags()
        for diag in diags:
            if len(diag) < 4:
                continue
            for i in range(len(diag) - 3):
                if diag[i:i+4] == [1, 1, 1, 1]:
                    return 1
                if diag[i:i+4] == [2, 2, 2, 2]:
                    return 2
            
        board_elements = [item for sublist in self.board.get_raw() for item in sublist]
        if 0 not in board_elements: # If all elements are filled, tie
            return 0
        return -1
        
    def board_copy(self):
        return self.board.copy()
    
    def __isvalid(self, col):
        if self.__lowest_row(col) == -1:
            return False
        return True
    
    def __lowest_row(self, col):
        for i in range(self.board.get_dim()[0]):
            if self.board.get_el(i, col) != 0:
                return (i - 1)
        return self.board.get_dim()[0] - 1 # if empty col

    def run(self, log):
        win = -1
        while win == -1:
            if log:
                print("Player 1 Move")
                self.board.display()

            move1 = self.player1.choose_move(self.board_copy())

            if self.__isvalid(move1):
                self.board.set_el(1, self.__lowest_row(move1), move1)
            else:
                print("Invalid move")
            
            if log:
                print("Player 1: Column {}".format(move1))

            
            win = self.__check_win()
            if win != -1:
                break

            if log:
                print("Player 2 Move")
                self.board.display()

            move2 = self.player2.choose_move(self.board_copy())
            if self.__isvalid(move2):
                self.board.set_el(2, self.__lowest_row(move2), move2)
            else:
                print("Invalid move")
            
            if log:
                print("Player 2: Column {}".format(move2))
            
            win = self.__check_win()
        

        if log:

            self.board.display()
            if win == 0:
                print("Tie!")
                return win
            
            print("Player {} wins!".format(win))
        return win





class Player:
    def __init__(self, strategy, num):
        self.num = num
        self.strategy = strategy
    
    def choose_move(self, board):
        return self.strategy(board, self.num)

def manual_strategy(board, player):
    # use command line to get input
    move = 0
    valid = False
    while not valid:
        move = input("Choose col: ")

        try:
            move = int(move)
            valid = True
        except:
            print("Invalid input")
    
    return move

def isvalid(board, column):
    if board.get_el(0, column) == 0:
        return True
    return False

def lowest_row(column):
    for i in range(len(column)):
        if column[i] != 0:
            return (i - 1)
    return len(column) - 1 # if empty col   

def random_strategy(board, player):
    # choose a random valid move
    cols = board.get_dim()[1]

    move = 0
    while True:
        move = random.randint(0, cols - 1)
        if isvalid(board, move):
            break
    return move

def decent_strategy(board, player):
    cols = board.get_dim()[1]
    rows = board.get_dim()[0]

    colstates = [True]*cols
    for c in range(cols):
        for r in range(rows):
            el = board.get_el(r, c)
            if el != player and el != 0:
                colstates[c] = False
                break

            if board.get_el(r,c) != 0 and r == 0:
                colstates[c] = False
                break
    for i in range(len(colstates)):
        if colstates[i]:
            return i
    return 0


# g = Game(Player(manual_strategy, 1), Player(decent_strategy, 2))
# g.run(True)

wins = 0
runs = 100
# g = Game(Player(random_strategy, 1), Player(decent_strategy, 2))

for i in range(runs):
    g = Game(Player(random_strategy, 1), Player(decent_strategy, 2))
    if g.run(False) == 2:
        wins += 1
print(wins/runs)
