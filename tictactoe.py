import random as rn
board= ['-','-','-',
        '-','-','-',
        '-','-','-']
        
game_on=True

def displaybaord():
    print(board[0] +'|'+ board[1] +'|'+ board[2])
    print(board[3] +'|'+ board[4] +'|'+ board[5])
    print(board[6] +'|'+ board[7] +'|'+ board[8])

def playgame():
    pos = int(input('Enter the position between 1-9:'))
    position = pos-1

    board[position]='x'
    displaybaord()
    
def complay():
    x = rn.randint(1,9)
    board[x]='o'
    print('\n')
    displaybaord()

def row():
    row1=board[0]==board[1]==board[2]!='-'
    row2=board[3]==board[4]==board[5]!='-'
    row3=board[6]==board[7]==board[8]!='-'
    if row1 or row2 or row3:
        game_on =False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    else:
        return None
    
def colum():
    colum1=board[0]==board[3]==board[6]!='-'
    colum2=board[1]==board[4]==board[7]!='-'
    colum3=board[2]==board[5]==board[8]!='-'
    if colum1 or colum2 or colum3:
        game_on =False
    if colum1:
        return board[0]
    elif colum2:
        return board[1]
    elif colum3:
        return board[2]

    else:
        return None
def diagonal():
    d1=board[0]==board[5]==board[8]!='-'
    d2=board[2]==board[5]==board[6]!='-'
    if d1 or d2 :
        game_on =False
    if d1:import time 
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

mark = None
def displaybaord():
    print(board[0] +'|'+ board[1] +'|'+ board[2] + '    1|2|3')
    print(board[3] +'|'+ board[4] +'|'+ board[5] + '    4|5|6')
    print(board[6] +'|'+ board[7] +'|'+ board[8] + '    7|8|9')

def playgame(mark):
    displaybaord()
    mark = str(mark)
    print(mark.upper(),'turn')
    pos = int(input('select position between 1-9:'))
    position = pos-1

    if board[position]=='X' or board[position]=='O':
        print("You can't go there. Go again.\n")
        time.sleep(0.5)
    else:

        board[position]=mark
    # t=cht()
    if '-' not in board:
        print('Tie')
        exit()
    w=chw()

    if w =='X':
        print('X won')
        exit()
    elif w=='O':
         print('O won')
         che=ch()
         if che==1:
            play()
         else:
            exit()
         
        

    print('\n')

def chw():
    x=xwin()
    o=owin()
    if x==True:
        return 'X'
    elif o==True:
        return 'O'

def xwin():
    column_1 = board[0] == board[3] == board[6] == "X"
    column_2 = board[1] == board[4] == board[7] == "X"
    column_3 = board[2] == board[5] == board[8] == "X"
    if column_1 or column_2 or column_3:
        return True
    row_1 = board[0] == board[1] == board[2] == "X"
    row_2 = board[3] == board[4] == board[5] == "X"
    row_3 = board[6] == board[7] == board[8] == "X"
    if row_1 or row_2 or row_3:
        return True
    diagonal_1 = board[0] == board[4] == board[8] == "X"
    diagonal_2 = board[2] == board[4] == board[6] == "X"
    if diagonal_1 or diagonal_2:
        return True
    
def owin():
    column_1 = board[0] == board[3] == board[6] == "O"
    column_2 = board[1] == board[4] == board[7] == "O"
    column_3 = board[2] == board[5] == board[8] == "O"
    if column_1 or column_2 or column_3:
        return True
    row_1 = board[0] == board[1] == board[2] == "O"
    row_2 = board[3] == board[4] == board[5] == "O"
    row_3 = board[6] == board[7] == board[8] == "O"
    if row_1 or row_2 or row_3:
        return True
    diagonal_1 = board[0] == board[4] == board[8] == "O"
    diagonal_2 = board[2] == board[4] == board[6] == "O"
    if diagonal_1 or diagonal_2:
        return True

def cht():
    r=row()
    c=colum()
    d=diagonal()
    if r==c==d==True:
        return True
    else:
        False

def colum():
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        return True
    else:
        return False

def row():
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        return True
    else:
        return False

def diagonal():
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        return True
    else:
        return False

def check():
    colum()
    row()
    dioganal()

def play():
    mark = 'O'
    playgame(mark)
    p2()
def p2():
    mark = 'X'
    playgame(mark)
    play()



play()
        