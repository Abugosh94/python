#defining user class
class User:
    #Create a file with the User class, including the __init__ and make_deposit methods
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    #Add a make_withdrawal method to the User class
    def make_withdrawl(self, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
            return self
        else:
            return "Insufficient funds"

    #Add a display_user_balance method to the User class
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        if(self.balance - amount > 0):
            self.balance -= amount
            other_user.balance += amount
            return self
        else:
            return "Insufficient funds"

#Create 3 instances of the User class    
Ali = User("Ali", "Ali@gmail.com")
Steven = User("Steven", "Steve@gmail.com")
Rachel = User("Rachel", "Rachel@gmail.com")


#Have the first user make 3 deposits and 1 withdrawal and then display their balance
Ali.deposit(5000).deposit(400).deposit(100).make_withdrawl(300).display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
Steven.deposit(3600).deposit(250).make_withdrawl(500).make_withdrawl(300).display_user_balance()


#Have the third user make 1 deposits and 3 withdrawals and then display their balance
Rachel.deposit(2780).make_withdrawl(150).make_withdrawl(390).make_withdrawl(758).display_user_balance()


#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
Ali.transfer_money(Rachel,500).display_user_balance()
Rachel.display_user_balance()
