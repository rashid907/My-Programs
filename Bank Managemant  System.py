import os
import random as rn
class bank():
    def __init__(self,name,balance,pin,acc):
        self.name = name
        self.balance = balance
        self.pin = pin    
        self.acc = acc

    def witdraw(self):
        print('Current balance:',self.balance)
        witdraw = int(input('Enter Amount to be Witdraw:'))
        if witdraw>self.balance:
            print('Not sufficent Amount')
            input('Press Enter to continue....')
        else:
            self.balance = (self.balance)-witdraw
            print('Witdraw Succesfull')
            print('Current balance:',self.balance)
            input('Press any key to continue....')   
    def deposit(self):
        print('Current balance:',self.balance)
        deposit = int(input('Enter the Amount to be Deposit:'))
        self.balance =self.balance+deposit
        print('Desposit Succesful')
        input('Press Enter to continue....')

    def transfer(self):
        os.system('cls')
        acc_no = int(input('Enter the Account number:'))
        for acc in account:
                if (acc.acc==acc_no):
                    amount = int(input('Enter the amount to be tranfer:'))
                    self.balance = self.balance+amount         
        
        print('There is no account with Acc no:',acc_no)
        
          
account = []
def check(detail):
    os.system('cls')
    c=input('Enter Your PIN:')
    if account[detail].pin==c:
        menu(detail)
    else:
        print('Incorrect Password!!')
        print('1. Try Again')
        print('2. Menu')
        x=int(input('Enter your choice:'))
        if x==1:
            check(detail)
        else:
            main()
def Password():
    pin = input('Make PIN Password(Pin Must be 4 Digit): ')
    if len(pin)<4:
        print('\n\nPlease Enter 4 Digit PIN ')
        Password()
    else:
        print('Account Added Succesfully')
        input('Press Enter to continue....')
        return pin
def menu(detail):
    os.system('cls')
    print('What you want to know about your Account?')
    print('1. Balance')
    print('2. Witdraw')
    print('3. Deposit')
    print('4. Tranfer Money')
    print('5. Delete Account')
    print('6. Exit')
    choice = int(input('Enter your choice:'))
    if choice==1:
        print('You have:',account[detail].balance,' in your Account')
        input('Press Enter to continue....')
        menu(detail)
    elif choice==2:
        account[detail].witdraw()
        menu(detail)
    elif choice==3:
        account[detail].deposit()
        menu(detail)
    elif choice==4:
        account[detail].transfer()
    elif choice==5:
        d = input('Are You Sure!! Wanna delete Account?(Y/N):')
        if d=='y' or d=='Y':
            account.pop(detail-1)
        elif d=='n' or d=='N':
            menu(detail)
    elif choice ==6:
        return
    else:
        print('Invalid Input')
i=0
def main():
    while True:
        os.system('cls')
        print('Welcome to Account!')
        print('1. Add Account')
        print('2. Account Detail')
        print('3. Exit')
        ch = int(input('Enter your choice:'))
        if ch==1:
            os.system('cls')
            acc = rn.randint(10,99)
            print('Add your Account')
            print('Your Account number is:',acc)
            name = input('Enter your Name:')
            balance = int(input('Enter your starting balance:'))
            pin = Password()
            account.append(bank(name,balance,pin,acc))
        elif ch==2:
            os.system('cls')
            if len(account)<=0:
                print('There is no Account!!')
                print('Please Add one..')
                input('Press any key to continue....')
                main()
            i=1
            for name in account:
                print(i,'.','Name:',name.name, '\nAccount no:',name.acc)
                i+=1
            detail = int(input('Select Account:'))
            check(detail-1)           
        elif ch==3:
            exit()
        else:
            print('Invalid Input')
        print('\n\n')
main()