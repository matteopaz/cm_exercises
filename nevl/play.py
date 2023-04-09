from helpers import load
from nn import fc
from tictactoe import TicTacToe, Player, manual_strategy, perfect

p1 = Player(fc(*load('./bestmodel.pkl')), 1, nn=True)
# p1 = Player(perfect, 1)
p2 = Player(manual_strategy, -1)
game = TicTacToe(p1, p2)
game.run(True)

