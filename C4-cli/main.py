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


def gameloop(board):
    
    win = False
    
    while win == False:
        ...
    
    ...






def main():
    print('Working')
    
    board_1 = empty_board()
    
    board_1[1][1] = PLAYER1
    
    print_board(board_1)
    
    
    print('End work')
    ...



if __name__ == "__main__":
    main()