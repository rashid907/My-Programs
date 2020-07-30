#Snake water gun Game 
import random as rn

op = ('s','w','g')
i = 0
point = 0
Lose =0
Draw =0
while(i<10):
    print('Enter option',i+1,'Option:') #User Input
    user = input()
    com = rn.choice(op)
    #print('Computer Choice:',com)
    if (user=='s' and com=='w'): #Snake>Water
        point = point +1    
    
    elif(user=='s' and com=='g'): #Snake<Gun
        Lose = Lose + 1

    elif(user=='s' and com=='s'):#Snake=Snake
        Draw = Draw +1

    elif(user=='g' and com=='w'): #Gun<Water
        Lose = Lose + 1

    elif(user=='g' and com=='s'): #Gun>Snake
        point = point + 1

    elif(user=='g' and com=='g'): #Gun=Gun
        Draw = Draw +1

    elif(user=='w' and com=='g'): #Water>Gun
        point = point + 1

    elif(user=='w' and com=='s'): #water<Snake
        Lose = Lose + 1

    elif(user=='w' and com=='w'): # Water=Water
        Draw = Draw +1

    else:
        print("Invalid Character")

    i = i+1
file = open('E:\\Rashid\\Python\\Files\\record.txt','r')
re = file.read()
file.close()
print('High Score:',re)
print('Your Win:',point,'Times')
print('You Lose:',Lose,'Times')
print('You Draw:',Draw,'Times')

if str(point)>re:
    file = open('E:\\Rashid\\Python\\Files\\record.txt','w+')#  
    file.write(str(point))
    # file.truncate()

file.close()