def game():
    import random
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    import chess
    board = chess.Board()
    while not board.is_checkmate() and not board.is_stalemate():
        move1 = chess.Move.from_uci(input('What move would you like to make? Input your answer as \'square1square2\', e.g. \'a2a3\' to move the piece at a2 to a3.'))
        if move1 in board.legal_moves:
            board.push(move1)
            print(board)
        else:
            print("Game ended due to illegal move.")
            break
        print("\n\n")
        while True:
            letter = random.choice(letters)
            number = random.choice(numbers)
            letter2 = random.choice(letters)
            number2 = random.choice(numbers)
            coord1 = str(str(letter) + str(number))
            coord2 = str(str(letter2) + str(number2))
            try:
                move2 = chess.Move.from_uci(str(coord1 + coord2))
            except:
                continue
            if move2 in board.legal_moves:
                board.push(move2)
                print(board)
                break
    if board.is_checkmate():
        print("You won!")
    elif board.is_stalemate():
        print("This game is a draw!")
game()
