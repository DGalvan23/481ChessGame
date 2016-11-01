import sys

from Game import Game
from Board import Board
from Piece import Piece

def moveWhite(board):
    savedState = board.saveState()
    score, move = heuristicWhite(board, 3, -float("inf"), float("inf"))
    print("score and move: ", score, move)
    board.restoreState(savedState)
    print('Moving: ', move)
    board.movePiece(move[0], move[1])
    print(board)

def moveBlack():
    print "Nothing happens here"	
    pass

def heuristicWhite(board, depth, alpha, beta):
    """Returns a tuple (score, bestMove) for the position at the given depth"""
    color = 'white'

    if depth == 0 or board.isCheckmate(color) or board.isCheckmate(Board.oppositeColor(color)) or board.isDraw():
        print('top kek')
        return (board.evaluate(color), None)
    else:
        print('Evaluating white else...')
        bestMove = None

        for move in board.legalMoves(color):
            print("The white move is: ", str(move[0]), str(move[1]))
            
            board.movePiece(move[0], move[1])   # It makes a move
            print("Alpha ",alpha, " Beta ", beta)
            score, move = heuristicBlack(board, depth - 1, alpha, beta)
            board.movePiece(move[1], move[0])
            print("Alpha ",alpha, " Beta ", beta)
            if score > alpha: # white maximizes her score
                alpha = score
                bestMove = move
            if alpha >= beta: # alpha-beta cutoff
                break

        return (alpha, bestMove)

def heuristicBlack(board, depth, alpha, beta):
    """Returns a tuple (score, bestMove) for the position at the given depth"""
    color = 'black'

    if depth == 0 or board.isCheckmate(color) or board.isCheckmate(Board.oppositeColor(color)) or board.isDraw():
        return (board.evaluate(color), None)
    else:
        print('Evaluating black else...')
        bestMove = None
        for move in board.legalMoves(color):
            print("The black move is: ", str(move[0]), str(move[1]))

            board.movePiece(move[0], move[1])
            score, move = heuristicWhite(board, depth - 1, alpha, beta)
            board.movePiece(move[1], move[0])
            if score < beta: # black minimizes his score
                beta = score
                bestMove = move
            if alpha >= beta: # alpha-beta cutoff
                break

        return (beta, bestMove)

def play(n, DEBUG):
    if DEBUG:
        board = Board()
        board.setup()

        startBoard = [
        ('H1', Piece(color='white', type='Rook')),
        ('E1', Piece(color='white', type='King')),
        ('E8', Piece(color='black', type='King'))]


        checkmateBoard = [
        ('A3', Piece(color='white', type='Rook')),
        ('C2', Piece(color='white', type='King')),
        ('A1', Piece(color='black', type='King'))]

        #board.restoreState(checkmateBoard) # Uncomment to inject a checkmate board
        board.restoreState(startBoard)
        print(board)

        # Play starts with white's turn


        # for loc, square in board.squares.items():
        # 	if square.isOccupied():
        		
        # 		piece = square.getPiece()
        			
        # 		if piece.getType() == 'Rook':
        # 			rookMoves = Game.generateRookMoves(piece, square)
        # 		if piece.getType() == 'King':
        # 			kingMoves = Game.generateKingMoves(piece, square)
		
		
        # evaluation(board)
        # print('Black in check: ', board.inCheck('black'))
    else:
        pass

    # Start playing!
    for i in range(n):
        if i % 2 == 0:
            moveWhite(board)
        else:
            moveBlack()
		
def alphabeta(position, depth, alpha, beta):
    """Returns a tuple (score, bestmove) for the position at the given depth"""
    if depth == 0 or position.is_checkmate() or position.is_draw():
        return (position.evaluate(), None)
    else: 
        if position.to_move == "white":
            bestmove = None
            for move in position.legal_moves():
                new_position = position.make_move(move)
                score, move = alphabeta(new_position, depth - 1, alpha, beta)
                if score > alpha: # white maximizes her score
                    alpha = score
                    bestmove = move
                    if alpha >= beta: # alpha-beta cutoff
                        break
            return (alpha, bestmove)
        else:
            bestmove = None
            for move in position.legal_moves():
                new_position = position.make_move(move)
                score, move = alphabeta(new_position, depth - 1, alpha, beta)
                if score < beta: # black minimizes his score
                    beta = score
                    bestmove = move
                    if alpha >= beta: # alpha-beta cutoff
                        break
            return (beta, bestmove)



def main(argv):

    print("\nWelcome to ChessPlayer")
    print("Created by Team Team at California State University, Fullerton")

    DEBUG = True

    ans = raw_input("\nPress Enter to begin the game...")

    #n = int(argv[0]) if len(argv) > 0 else 35
    with open("config.txt","r") as ifh:
        n = int(ifh.readline())

    if ans == "":
        print('Beginning the chess game...\n')
        play(n, DEBUG)
    else:
        print("Goodbye")



if __name__ == "__main__":

    main(sys.argv[1:])

