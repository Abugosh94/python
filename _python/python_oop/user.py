#defining user class
class User:
    #Create a file with the User class, including the __init__ and make_deposit methods
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    #Add a make_withdrawal method to the User class
    def make_withdrawl(self, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
        else:
            return "Insufficient funds"

    #Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
            other_user.balance += amount
        else:
            return "Insufficient funds"

#Create 3 instances of the User class    
Ali = User("Ali", "Ali@gmail.com")
Steven = User("Steven", "Steve@gmail.com")
Rachel = User("Rachel", "Rachel@gmail.com")


#Have the first user make 3 deposits and 1 withdrawal and then display their balance
Ali.deposit(5000)
Ali.deposit(400)
Ali.deposit(100)
Ali.make_withdrawl(300)
Ali.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
Steven.deposit(3600)
Steven.deposit(250)
Steven.make_withdrawl(500)
Steven.make_withdrawl(300)
Steven.display_user_balance()


#Have the third user make 1 deposits and 3 withdrawals and then display their balance
Rachel.deposit(2780)
Rachel.make_withdrawl(150)
Rachel.make_withdrawl(390)
Rachel.make_withdrawl(758)
Rachel.display_user_balance()


#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
Ali.transfer_money(Rachel,500)
Ali.display_user_balance()
Rachel.display_user_balance()
