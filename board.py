from copy import deepcopy

class Board():
    def __init__(self):
        self.matrix = [[" "," "," "],[" "," "," "],[" "," "," "]]


    def isFull(*board):
        board = deepcopy([*board[1:4]])
        for row in board:
            for col in row:
                if col == ' ':
                    return False
        return True


    def checkWinner(*board):
        board = deepcopy([*board[1:4]])

        if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
            return board[0][0]
        if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
            return board[1][0]
        if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
            return board[2][0]
        if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
            return board[0][0]
        if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
            return board[0][1]
        if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
            return board[0][2]
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            return board[0][2]

    def possiblePlays(self, *board):
        board = deepcopy([*board])
        plays = []
        for i in range (0, 3):
             for j in range(0,3):
                 if board[i][j] == " ":
                     plays.append([i, j])
        print (plays)
        return plays

    def play(self, *board, pos, player):
        board = deepcopy([*board])
        posx, posy = pos[0], pos[1]
        board[posx][posy] = player
        return board

    def minimax(self, *board, player, me, maxdepth=9):
        board = deepcopy([*board])
        w = self.checkWinner(*board)
        if w == me: return 1
        if w != me and not self.isFull(*board): return -1
        if self.isFull([*board]): return 0

        plays = self.possiblePlays([*board])

        if player == me: #MAX
            best = float("-inf")
            for p in plays:
                result = play([*board], plays[p], player)
                if player == 'X':
                    value = minimax(result, player = 'O', me = me)
                else:
                    value = minimax(result, player = 'X', me = me)
                if value > best:
                    best = value
            return best
        else:                #MIN
            best = float("-inf")
            for p in plays:
                result = play([*board], plays[p], player)
                if player == 'X':
                    value = minimax(result, player = 'O', me = me)
                else:
                    value = minimax(result, player = 'X', me = me)
                if value < best:
                    best = value
            return best

    def bestAction(self, *board, player): #returns best action
        board = deepcopy([*board])
        plays = self.possiblePlays(*board)
        print(board)
        #print(player)
        best = float('-inf')
        if player == 'O':
            player = 'X'
        else:
            player = 'O'

        for p in plays:
            result = self.play(*board, pos=p, player=player)
            value = self.minimax(*result, player = player, me=player)
            if value > best:
                best = value
                bestAct = p
        return bestAct

b = Board()

pp = b.bestAction(["O","X","O"],[" ","X", " "],[" "," "," "], player = "O")

print (pp)
