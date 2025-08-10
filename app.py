

board = [
    ["r","n","b","q","k","b","n","r"],
    ["p","p","p","p","p","p","p","p"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-"],
    ["P","P","P","P","P","P","P","P"],
    ["R","N","B","Q","K","B","N","R"]
]

def print_board(board):
    for row in board:
        for square in row:
            print(square, end=" ")
        print()  # Print a newline after each row

def parse_move(move):
    move = move.strip()  # Clean up whitespace
    if not move:
        raise ValueError("Move cannot be empty.")
    # Should consider validating what we can about the notation syntax right away
    # e.g. should always start with a valid piece or destination square

    ## Initialize move information dictionary
    move_info = {
        "notation": move,
        "piece": None,
        "destination": None,
        "castle": None,
        "is_promotion": False,
        "promotion_piece": None,
        "is_capture": False,
        "is_check": False,
        "is_checkmate": False,
        "is_good_move": False,
        "is_bad_move": False
    }

    ## Handle ancillary move information & normalize move notation
    if "+" in move:
        move = move.replace("+", "")  # Remove the check indicator for processing
        move_info["is_check"] = True
    if "#" in move:
        move = move.replace("#", "")  # Remove the checkmate indicator for processing
        move_info["is_checkmate"] = True
    if "x" in move:
        move = move.replace("x", "")  # Remove the capture indicator for processing
        move_info["is_capture"] = True
    if "!" in move:
        move = move.replace("!", "")  # Remove the good move indicator for processing
        move_info["is_good_move"] = True
    if "?" in move:
        move = move.replace("?", "")  # Remove the bad move indicator for processing
        move_info["is_bad_move"] = True

    ## Handle castling
    if move.lower() in ("o-o","0-0","oo","00"):
        move_info["castle"] = "kingside"
        return move_info
    elif move.lower() in ("o-o-o","0-0-0","ooo","000"):
        move_info["castle"] = "queenside"
        return move_info

    ## Handle pawn promotion
    if "=" in move:
        promotion_piece = move.split("=")[-1].upper()
        if promotion_piece not in ("Q", "R", "B", "N"):
            raise ValueError("Invalid promotion piece. Must be Q, R, B, or N.")
        else:
            move_info["is_promotion"] = True
            move_info["promotion_piece"] = promotion_piece  
        move = move.split("=")[0]  # Remove the promotion part for further processing
    
    ## Determine piece and destination
    if len(move) < 2:
        raise ValueError("Invalid move notation. Length must be at least 2 characters. You entered: " + move_info["notation"])
    if len(move) > 4:
        raise ValueError("Invalid move notation. Length of piece & destination square info cannot exceed 4 characters. You entered: " + move_info["notation"])
    
    if move[0] in ("K", "Q", "R", "B", "N"):
        move_info["piece"] = move[0].upper()
    elif move[0] in ("a","b","c","d","e","f","g","h"):   # Assume it's a pawn move  
        move_info["piece"] = "P"
    else:
        raise ValueError(f"Invalid piece notation. Must be K, Q, R, B, N, or a pawn move. You entered: {move_info["notation"]}")
    # should add regex to validate destination square syntax
    if move[-2] not in ("a", "b", "c", "d", "e", "f", "g", "h") or not move[-1].isdigit() or int(move[-1]) < 1 or int(move[-1]) > 8:
        raise ValueError(f"Invalid destination square notation. Must be a valid square like e4, d5, etc. You entered: {move_info['notation']}")
    move_info["destination"] = move[-2:]  # Last two characters are the destination square

    return move_info
    

def move_piece(piece, destination):
    pass
    
    piece = move[0].upper()  # Assuming the first character is the piece type
    destination = move[1:]  # The rest is the destination square
    return piece, destination


## Main Game
print("Welcome to Text-Based Chess!")
print("Here is the initial board setup:")
print_board(board)

while True:
    move = input("Enter your move (e.g., e2 e4) or 'exit' to quit: ")
    if move.lower() == 'exit':
        print("Exiting the game. Goodbye!")
        break
    try:
        move_info = parse_move(move)
    except ValueError as e:
        print(f"Error parsing move: {e}")
        continue
    # Here you would normally process the move, update the board, and check for game status.
    # For now, we will just print the move.
    print(f"Parsed move info: \n{move_info}")
    # print(f"You entered the move: {move}")