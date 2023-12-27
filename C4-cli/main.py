import sys


# params
BOARD_HEIGHT: int = 6
BOARD_WIDTH: int = 7

PLAYER0 = 'O'
PLAYER1 = 'X'

INBETWEENCHR = ' | '

STATUS_INIT: dict = {'win': False, 'next': PLAYER1}


def empty_board(height: int = BOARD_HEIGHT, width:int = BOARD_WIDTH) -> list:
    ''' Simple function to generate board as list of list of empty string charcters '''
    board = [[' ' for _ in range(width)] for _ in range(height)]
    return board

def print_board(board: list, status: dict = STATUS_INIT):
    ''' Simple function to print board to CLI '''
    print(f"Win is: {status['win']} & Next player is: {status['next']}")
    print(f"1   2   3   4   5   6   7")
    
    for row in board:
        out = INBETWEENCHR.join(row)  # Join the characters in the row with the INBETWEENCHR separator
        print(out)  # Print the joined row
    
    ...

def drop_piece(board: list, player:str = 'D', col: int = 1):
    ''' Simple function for dropping pieces
            default player is 'D' == de-bugger
            default col is 1 for de-bugging
        IN:
        board: l.o.l. of str
        player: str ('O' or 'X')
        col: int (1 - 7)
        OUT:
        board: l.o.l. of str
        '''
    row = len(board) - 1  # Get the last row index
    
    while row >= 0:
        if board[row][col-1] == ' ':  # Check if the cell is empty
            board[row][col-1] = player  # Place the player's piece in the cell
            break
        row -= 1  # Move to the previous row
    
    return board

def is_winner(board, player):
    # Check for four in a row horizontally
    for row in board:
        if player * 4 in "".join(row):
            return True

    # Check for four in a row vertically
    for col in range(7):
        if player * 4 in "".join(board[row][col] for row in range(6)):
            return True

    # Check for four in a row diagonally (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if player * 4 in "".join(board[row + i][col + i] for i in range(4)):
                return True

    # Check for four in a row diagonally (top-right to bottom-left)
    for row in range(3):
        for col in range(3, 7):
            if player * 4 in "".join(board[row + i][col - i] for i in range(4)):
                return True

    return False






def gameloop(board):
    
    win = False
    
    while win == False:
        ...
    
    ...








def main():
    
    ...



if __name__ == "__main__":
    main()