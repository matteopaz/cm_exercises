
from matrix import Matrix
import random
import matplotlib.pyplot as plt

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
        
        board_elements = [item for sublist in self.board.get_raw() for item in sublist]
        if 0 not in board_elements: # If all elements are filled, tie
            return 0
        return -1
    
    def run(self, log):
        win = -1 # -1: In progress, 0: Tie, 1: Player 1, 2: Player 2
        while win == -1:
            if log:
                print("start move")
                self.board.display()

            move1 = self.player1.choose_move(self.board_copy())
            if self.__isvalid(move1):
                self.board.set_el(1, move1[0], move1[1])
            if log:
                print("move 1")
                self.board.display()

            win = self.__check_win()
            if win != -1:
                break

            move2 = self.player2.choose_move(self.board_copy())
            if self.__isvalid(move2):
                self.board.set_el(2, move2[0], move2[1])
            if log:
                print("move 2")
                self.board.display()

            win = self.__check_win()
            if win != -1:
                break
        
        if win != 0 and log:
            print("Player {} wins!".format(win))
        elif log:
            print("Tie!")
        return win


class Player:
    def __init__(self, strategy_function, num):
        self.num = num
        self.move = strategy_function
    
    def choose_move(self, board):
        return self.move(board, self.num)

def possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board.get_el(i, j) == 0:
                moves.append([i, j])
    return moves

def random_strategy(board, player):
    # choose random move from available moves
    moves = possible_moves(board)
    if len(moves) == 0:
        return [0, 0]
    return random.choice(moves)

def decent_strategy(board, player):
    other_player = 1 if player == 2 else 2

    if board.get_el(1, 1) == 0: # get center
        return [1, 1]
    
    lines = []
    for i in range(3):
        row = board.get_row(i)
        col = board.get_col(i)
        if (row.count(player) == 2) and row.count(0) == 1:
            lines.append([i, row.index(0)])
        if (col.count(player) == 2) and col.count(0) == 1:
            lines.append([col.index(0), i])
    for i in range(1,3):
        diag = board.get_diag(i)
        if (diag.count(player) == 2) and diag.count(0) == 1:
            if i == 1:
                lines.append([diag.index(0), diag.index(0)])
            else:
                lines.append([diag.index(0), 2 - diag.index(0)])
    if len(lines) > 0:
        return random.choice(lines)
    else:
        return random_strategy(board, player)


    



def manual_strategy(board, player):
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

p2 = Player(manual_strategy, 2)
p1 = Player(decent_strategy, 1)
g = Game(p1, p2)
g.run(True)

# games = 100
# p1_wins = 0
# p2_wins = 0
# ties = 0
# for i in range(games):
#     g = Game(p1, p2)
#     result = g.run(False)
#     if result == 1:
#         p1_wins += 1
#     elif result == 2:
#         p2_wins += 1
#     else:
#         ties += 1
# print("Player 1 wins: {}%".format(p1_wins / games * 100))
# print("Player 2 wins: {}%".format(p2_wins / games * 100))
# print("Ties: {}%".format(ties / games * 100))
