#-------------------Number Guessing Game-------------
'''In this Game Computer generate a number and User has to guess it.
 Game Has 3 level's :-
 1.Easy(15 Chance):Anyone can guess it
 2.Medium(10 Chance): Smart user can guss it
 3.Hard(5 Chance):You can't
'''
import random  #Modul for Generating Random Number

x = random.randint(1,100) #Generating Random Number Between 1 to 100
i = 0 

print("Number Guessing Game!!") #Introducing
print("1. Easy(15 Chance)")     #For Easy Game       
print("2. Medium(10 Chance)")   #For Medium Game     
print("3. Hard(5 Chance)")      #For Hard Game 
a = int(input("Enter your Choice:")) #Asking User for Option
if (a==1):                                #Checking For 1st Option
    chance = 15                           #In Easy game you have 15 chances
    while (i<chance):                     #Check for Condition
        print("Chance Left:",chance-i)
        n = int(input("Enter the no.:"))

        if (n>x):
            print("Number is greater!!")

        elif (n<x):
            print("Number is smaller!!")

        elif (n==x):
            print("You won!! with ",chance-i,"Chance Left")
            exit()

        i = i+1


elif (a==2):
    chance = 10
    while (i<chance):
        print("Chance Left:",chance-i)
        n = int(input("Enter the no.:"))

        if (n>x):
            print("Number is greater!!")

        elif (n<x):
            print("Number is smaller!!")

        elif (n==x):
            print("You won!! with ",chance-i,"Chance Left")
            exit()

        i = i+1


if (a==3):
    chance = 5
    while (i<chance):
        print("Chance Left:",chance-i)
        n = int(input("Enter the no.:"))

        if (n>x):
            print("Number is greater!!")

        elif (n<x):
            print("Number is smaller!!")

        elif (n==x):
            print("You won!! with ",chance-i,"Chance Left")
            exit()

        i = i+1

if (i==6,11,16):
    print("You Lose!!")
    


    

    



