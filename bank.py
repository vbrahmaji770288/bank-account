
# ''''''''''''''''''''BMS''''''''''''''''''''''
class account():
    def __init__(self ,username,password,balance=0):
        self.username=username
        self.password=password
        self.balance=balance
        self.mini_state=[]
    def credit (self,):
        amount=int(input("enter the credit amount"))
        if amount<0:
            print("valid number")
        else:
            self.balance+=amount
            self.mini_state.append(f"credit amount{amount}")
            print("credit successful")
            print(f"avalaible balance amount{self.balance}")

    def debit(self,):
        amount=int(input("enter the debit amount"))
        if amount<0:
            print("enter valid number")
        elif amount>self.balance:
            print("infacient")
        else:
            self.balance-=amount
            self.mini_state.append(f"debit amount{amount}")
            print(f"avliable amount{self.balance}")

    def balanc(self,):
        print(f"balnce amount{self.balance}")

    def ministate(self,):
        for i in self.mini_state:
            print(i)
        
    def exit(self,):
        print("thank for visiting")

class SavingsAccount(account):

    def __init__(self, username, password, balance=0):

        super().__init__(username, password, balance)
    def show_account_type(self):
    
            print("Account Type: Savings Account")
class bankstatement():
    def __init__(self,):
        self.account={}

    def create_account(self, username, password):
        if username in self.account:
            print("already exit")
        else:
            self.account[username]=account(username,password)
            print("create account successful")

    def login(self,username,password):

            if username in self.account:
                account=self.account[username]
                if account.password==password:
                    print("login successful")
                    return account
                else:
                    print("invalid password")
            else:
                print("invalid username")
                return None
bank=bankstatement() 

while True:
    print("\n")
    print("1 create account")
    print("2,login")
    print("3,exit")

    choice=input("enter the number ")
    if choice=="1":
        username=input("enter the username")
        password=input("enter the password ")
        bank.create_account(username,password)
    elif choice=="2":
        username=input("enter the username")
        password=input("enter the password")
        account=bank.login(username,password)
        if account is not None:
            while True:
                print("\n")
                print("banksystem")
                print("1,credit")
                print("2,debit")
                print("3 balance")
                print("4,ministatement")
                print("5 exit")
                choice=input("enter the number 1 to 4")
                if choice=="1":
                 account.credit()
                elif choice=="2":
                    account.debit()
                elif choice=="3":
                    account.balanc()
                elif choice=="4":
                    account.ministate()
                elif choice=="5":
                    account.exit()
                    break
                
                
                else:
                    print("enter valid number")
    elif choice=="3":
        print("thank for visiting")
        break

        



    

    



    
