import random as rn

runop = (1,2,3,4,6,)
turn = None

def playerplay(rr):
    i=0
    run = 0
    while(i<6):
        if turn==True:
            re = rr-run
            if rr>=1:
                if re<=0:
                    if rr==run: 
                        break
                    break
            print('Runs Remaining:',re,'\nball left:',6-i,'Balls\n')
                
        print('Select run between:',runop)
        n = int(input())
        x = rn.choice(runop)
        if n==x:
            print('Out!!\n')
            print('You make',run,'Runs')
            return run

        run = run + int(n)


        i+=1
    print('You make',run,'Runs\n')
    return run

def complay(rr):
    i=0
    comrun = 0
    while(i<6):
        if turn==True:
            ree = rr-comrun
            if rr>=1:
                if ree<=0:
                    if rr==comrun:
                        break
                    break
            print('Runs Remaining:',ree,'\nBall left:',6-i,'Balls\n')
        print('Select your choice between:',runop)
        a = int(input())
        x = rn.choice(runop)
        if a==x:
            print('Out!!\n')
            print('Computer make',comrun,'Runs')
            return comrun

        comrun = comrun + int(x)
        
        i+=1
    print('Computer make',comrun,'Runs\n')
    return comrun
    

# player = None

while True:
    turn = None
    key = int(input('1.Bat.\n2.Bowl\nWhat You Want :'))
    if key==1:
        print('Your bat First')
        p=playerplay(0)
        turn = True
        print('Computer had to make',p,'run in 6 balls\n')
        print('Needed Strike Rate:',(p//6)*100)
        c=complay(p)
        if p > c:
             print('Player win by:',(p-c))
        elif p==c:
            print('Mathc tie')
        else:
            print('Computer wins')
    else:
        print('You Bowl First')
        q=complay(0)
        turn = True
        print('Player had to make',q,'run in 6 balls\n')
        print('Needed Strike Rate:',(q/6)*100)
        r=playerplay(q)
        if q > r:
            print('computer wins')
        elif q==r:
            print('Mathc tie')
        else:
            print('player wins by:',(r-q))
    print('\n\n')



