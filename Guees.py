import random # Modul for Generating Random Number

x = random.randint(1,100) #Generating Random Number Between 1 to 100
i = 0

print("Number Guessing Game!!") #Introducing
print("1. Easy(15 Chance)")         
print("2. Medium(10 Chance)")       
print("3. Hard(5 Chance)")
a = int(input("Enter your Choice:"))
if (a==1):
    chance = 15
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
    


    

    



