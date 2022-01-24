        
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

