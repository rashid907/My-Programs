#-------------Modules--------
import time             #Time Module for timer

#-------------Global Variable----------
board = ['-','-','-',   #List for Baord
         '-','-','-',
         '-','-','-',]

mark = None             #Mark variable. It should be X or O


#--------------Functions----------------------

def displayboard(): #Function for print Baord
    print(board[0]+'|'+board[1]+"|"+board[2],'         1|2|3')
    print(board[3]+'|'+board[4]+"|"+board[5],'         4|5|6')
    print(board[6]+'|'+board[7]+"|"+board[8],'         7|8|9')


def playgame(mark):     #Function for Playing Game. It take argument Mark
    displayboard()
    print('\n\n')
    print(mark + ' Turn')
    n= int(input('Select the postion between 1-9:'))
    pos = n-1
    if board[pos]!='-':
        print("Can't go there!! Try Again")
        time.sleep(0.8)
        if mark =='X':
            p1()
        else:
            p2()
    else:
        board[pos]=mark
    if '-' not in board:
        displayboard()
        print('\n')
        print('Tie')
        exit()
    win=checkwin() 
    if win=='X':
        displayboard()
        print('\n')
        print(win+' Win')
        exit()
    elif win=='O':
        displayboard()
        print('\n')
        print(win+' Win')
        exit()

def row():          #Fucntion for checking row
    r1 = board[0]==board[1]==board[2]!='-'
    r2 = board[3]==board[4]==board[5]!='-'
    r3 = board[6]==board[7]==board[8]!='-'
    if r1:
        return board[0]
    if r2:
        return board[3]
    if r3:
        return board[6]
def colum():        #Fucntion for checking colum
    colum1=board[0]==board[3]==board[6]!='-'
    colum2=board[1]==board[4]==board[7]!='-'
    colum3=board[2]==board[5]==board[8]!='-'
    if colum1:
        return board[0]
    elif colum2:
        return board[1]
    elif colum3:
        return board[2]
    else:
        return None
def diagonal():     #Fucntion for checking diagonal
    d1=board[0]==board[5]==board[8]!='-'
    d2=board[2]==board[5]==board[6]!='-'
    if d1:
        return board[0]
    elif d2:
        return board[2]
    else:
        return None
def checkwin():     #Fucntion for checking Win
    r=row()
    c=colum()
    d=diagonal()
    if r!=None:
        return r
    elif c!=None:
        return c
    elif d!=None:
        return d
    else:
        return None
def p1():           #Fucntion for starting game by mark X
    mark='X'
    playgame(mark)
    p2()
def p2():           #Fucntion for mark O
    mark = 'O'
    playgame(mark)
    p1()

#------------Execution Start from here-------------
p1()