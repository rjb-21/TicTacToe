# Tic Tac Toe Game

# Import function to clear output
from IPython.display import clear_output

# Print board function
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


def display_board(board):
    
        clear_output()
        print(board[1] + '|' + board[2] + '|' + board[3])
        print(board[4] + '|' + board[5] + '|' + board[6])
        print(board[7] + '|' + board[8] + '|' + board[9])


# Choose player mark
def player_input():
    
    # INITIAL VALUES
    choice = ''
    
    # CONTITIONS TO CHECK
    while choice != 'X' and choice != 'O':
        
        choice = input("Player 1, please select mark (X or O): ").upper()
            
    player1 = choice
    
    if player1 =='X':
        player2 =  'O'
    else:
        player2 = 'X'
    
    return (player1,player2)


# Place mark on board function
def place_marker(board, marker, position):
 
    board[position] = marker


# Check win
def win_check(board, mark):
    
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else: 
        return False 


# Start player random choice
from random import randint

def choose_first():
    return randint(1,2)


# Check free space
def space_check(board, position):
    
    if board[position] == ' ':
        return True
    else:
        return False


#Chceck full board
def full_board_check(board):
        
    if ' ' in board:
        return False
    else:
        return True


# Position choice
def player_choice(board,current_player,mark):
    
    acceptable_range = range(1,10)
    within_range = False
    space_free = False
    position = 'Wrong'
    
    # CHECK INPUT
    while position.isdigit() == False or within_range == False or space_free == False :
        
        position = input(f" Player{current_player} ({mark}) choose your next position (1-9): ")
        
        if position.isdigit() == True:
            if int(position) in acceptable_range:
                within_range = True
                space_free = space_check(board, int(position))
    
    return int(position)


# Ask players if they want to play again
def replay():

    choice = 'Wrong'

    while choice != 'Y' and choice != 'N':
        
        choice = input("Do you want to play again (Y or N)?: ").upper()
    
    return choice == 'Y'


#Game
reply = True
    
while reply == True:

    #Start values
    full_board = False
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    play = False
    win1 = False
    win2 = False

    print('Welcome to Tic Tac Toe!')

    players = player_input()

    current_player = choose_first()

    if players[0] == 'X' or players[0] == 'O':
        play = True


    while play == True:
    #print("OK")
    #play = False
       
        while (full_board != True and win1 != True and win2 != True):
            display_board(board)
        
        #Player 1 turn
            if current_player == 1:           
                position = player_choice(board,current_player,players[0])
                place_marker(board,players[0],position)
                win1 = win_check(board,players[0])
                full_board = full_board_check(board)
                current_player = 2
        #Player 2 turn
            elif current_player == 2:
                position = player_choice(board,current_player,players[1])
                place_marker(board,players[1],position)
                win2 = win_check(board,players[1])
                full_board = full_board_check(board)
                current_player = 1
                
        display_board(board)    
        if win1 == True:
            print("Player 1 win!")
            play = False
        elif win2 == True:
            print("Player 2 win!")
            play = False
        elif win1 == False and win2 == False and full_board == True:
            print("Draw!")
            play = False
        else: 
            pass
    
    reply = replay()
