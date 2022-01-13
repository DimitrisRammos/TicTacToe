import pygame
def draw():
    board = ''

    for i in range(-1,6):

        if i%2==0:
            board += '|     ' * 4
            board += '\n|     |     |     |'

        else:
            board += ' ____ ' * 3

        board += '\n'
    print (board)


def draw_new(board):
    b = ''
    start = 0
    for i in range(-1,6):
        if i %2 == 0:
            b += '|     ' * 4
            List = board[start]
            p1 = List[0]
            if p1 == None:
                b += '\n|     |'
            
            elif p1 == "X":
                b += '\n|  X  |'
            else:
                b += '\n|  O  |'
            
            
            p2 = List[1]
            if p2 == None:
                b += '     |'
            
            elif p2 == "X":
                b += '  X  |'
            else:
                b += '  O  |'
            
            
            p3 = List[2]
            if p3 == None:
                b += '     |'
            
            elif p3 == "X":
                b += '  X  |'
            else:
                b += '  O  |'
            
            start += 1
            
        else:
            b += ' ____ ' * 3
            
        b += '\n'
    print(b)
    
    
def create_board():
    board = {}
    for i in range(3):
        board[i] = [None, None, None]
    return board


def update_board( board, x, y, symbol):
    element = symbol
    List = board[x - 1]
    
    if List[y - 1] != None:
        return None
    
    List[y - 1] = element
    board[x-1] = List
    print(board)
    draw_new( board)
    return board    
    
    
def check_board( board):
    check = "X"
    #check first line
    List = board[0]
    if( List[0] == "X" and List[1] == "X" and List[2] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List[0] == "O" and List[1] == "O" and List[2] == "O"):
        print("Player 2 win the game!!!")
        return True

    #check second line
    List = board[1]
    if( List[0] == "X" and List[1] == "X" and List[2] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List[0] == "O" and List[1] == "O" and List[2] == "O"):
        print("Player 2 win the game!!!")
        return True

    #check third line
    List = board[2]
    if( List[0] == "X" and List[1] == "X" and List[2] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List[0] == "O" and List[1] == "O" and List[2] == "O"):
        print("Player 2 win the game!!!")
        return True
    
    List_1 = board[0]
    List_2 = board[1]
    List_3 = board[2]

    #check first katheti-line
    if( List_1[0] == "X" and List_2[0] == "X" and List_3[0] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List_1[0] == "O" and List_2[0] == "O" and List_3[0] == "O"):
        print("Player 2 win the game!!!")
        return True
    
    #check second katheti-line
    if( List_1[1] == "X" and List_2[1] == "X" and List_3[1] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List_1[1] == "O" and List_2[1] == "O" and List_3[1] == "O"):
        print("Player 2 win the game!!!")
        return True
        
    #check third katheti-line
    if( List_1[2] == "X" and List_2[2] == "X" and List_3[2] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List_1[2] == "O" and List_2[2] == "O" and List_3[2] == "O"):
        print("Player 2 win the game!!!")
        return True
    
    
    #check the first side-line
    if( List_1[0] == "X" and List_2[1] == "X" and List_3[2] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List_1[0] == "O" and List_2[1] == "O" and List_3[2] == "O"):
        print("Player 2 win the game!!!")
        return True
    
    #check the second side-line
    if( List_1[2] == "X" and List_2[1] == "X" and List_3[0] == "X"):
        print("Player 1 win the game!!!")
        return True
    elif( List_1[2] == "O" and List_2[1] == "O" and List_3[0] == "O"):
        print("Player 2 win the game!!!")
        return True
    
    return False
    
    
def two_players():
    print("Start Game")
    board = create_board()
    draw()
    
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    while(1):
        
        print("\nFirst Player with X")
        x = int(input("Give x   "))        
        y = int(input("Give y   "))  
        board = update_board( board, x, y, "X")
        while board == None:
            
            print("\nWrong Input for Player 1, Please try again")
            x = int(input("Give x   "))        
            y = int(input("Give y   "))  
            board = update_board( board, x, y, "X")
        
        if check_board( board) == True:
            break
        
        
        print("\nSecond Player with O")
        x = int(input("Give x   "))        
        y = int(input("Give y   "))  
        board = update_board( board, x, y, "O")
        while board == None:
            
            print("\nWrong Input for Player 2, Please try again")
            x = int(input("Give x   "))        
            y = int(input("Give y   "))  
            board = update_board( board, x, y, "O")

        if check_board( board) == True:
            break
        
        
def one_player():
    print("Start Game")
    


if __name__ == "__main__":
    while(1):
        
        players = int(input("How many players?\n"))
        if players == 2:
            two_players()
            break
        elif players == 1:
            one_player()
            break
        else:
            print("Wrong input")

        