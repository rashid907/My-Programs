import time
def sum(a,b):
        c = (a+b)
        return (c)

def su(a,b):
        c = (a-b)
        return (c)

def dv(a,b):
        c = (a/b)
        return (c)

def mu(a,b):
        c = (a*b)
        return (c)

def sqr(a):
        return(a*a)

def cub(a):
        return (a*a*a)

def menu():
        print('\n')
        print("Welcome to Calculator v1.0")
        print("What you want to Calculate??")
        print("Press + for Addition")
        print("Press - for Subtraction")
        print("Press x for Multiplication")
        print("Press / for Division")
        print('Press * for Square')
        print('Press ** for Cube')
        print('Press ! for exit')
        n = input("Enter your choice:")
        return n

def choice(n):
        if (n == '+'):
                x = float(input("Enter 1st number:"))
                y = float(input("Enter 2nd number:"))
                print(sum(x,y))

        elif (n == "-"):
                x = float(input("Enter 1st number:"))
                y = float(input("Enter 2nd number:"))
                print(su(x,y))

        elif (n == "x"):
                x = float(input("Enter 1st number:"))
                y = float(input("Enter 2nd number:"))
                print(mu(x,y))

        elif (n == "/"):
                x = float(input("Enter 1st number:"))
                y = float(input("Enter 2nd number:"))
                print(dv(x,y))

        elif (n== '*'):
                x = float(input("Enter the number:"))
                print(sqr(x))

        elif (n=='**'):
                x = float(input("Enter the number:"))
                print(cub(x))
        
        elif (n=='!'):
            exit()
        else :
            print("Invalid Character")



