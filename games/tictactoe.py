
from matrix import Matrix
import random

class Game:
    def __init__(self, player1, player2):
        self.board = Matrix(3, 3, 0)
        self.player1 = player1
        self.player2 = player2
    
    def board_copy(self):
        return self.board.copy()
    
    def __isvalid(self, move):
        x = move[0]
        y = move[1]
        if self.board.get_el(x, y) != 0:
            return False
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        if not isinstance(x, int) or not isinstance(y, int):
            return False
        return True
    
    def __check_win(self):
        for i in range(3):
            if self.board.get_row(i) == [1, 1, 1]:
                return 1
            if self.board.get_row(i) == [2, 2, 2]:
                return 2
            if self.board.get_col(i) == [1, 1, 1]:
                return 1
            if self.board.get_col(i) == [2, 2, 2]:
                return 2

        if self.board.get_diag(1) == [1, 1, 1]:
            return 1
        if self.board.get_diag(1) == [2, 2, 2]:
            return 2
        if self.board.get_diag(2) == [1, 1, 1]:
            return 1
        if self.board.get_diag(2) == [2, 2, 2]:
            return 2

        return -1
    
    def run(self, log):
        win = -1 # -1: In progress, 0: Tie, 1: Player 1, 2: Player 2
        while win == -1:
            move1 = self.player1.choose_move(self.board_copy())
            if self.__isvalid(move1):
                self.board.set_el(1, move1[0], move1[1])
            
            move2 = self.player2.choose_move(self.board_copy())
            if self.__isvalid(move2):
                self.board.set_el(2, move2[0], move2[1])

            if log: 
                self.board.display()

            win = self.__check_win()
        if win != 0:
            print("Player {} wins!".format(win))
        else:
            print("Tie!")


class Player:
    def __init__(self, strategy_function):
        self.move = strategy_function
    def choose_move(self, board):
        return self.move(board)

def random_strategy(board):
    # choose random move from available moves
    moves = []
    for i in range(3):
        for j in range(3):
            if board.get_el(i, j) == 0:
                moves.append([i, j])
    return random.choice(moves)


def manual_strategy(board):
    # use command line to get input
    move = [0, 0]
    valid = False
    while not valid:
        move[0] = input("Choose row (0 to 2): ")
        move[1] = input("Choose column (0 to 2): ")
        try:
            move[0] = int(move[0])
            move[1] = int(move[1])
            valid = True
            if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
                print("Invalid input!")
                valid = False
        except:
            print("Invalid input")
    
    return move

p2 = Player(random_strategy)
p1 = Player(manual_strategy)
g = Game(p1, p2)
g.run(True)