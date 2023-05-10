#defining user class
class User:
    #Update the User class __init__ method
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"Savings": BankAccount(int_rate=0.03, balance =0), "Current": BankAccount(int_rate=0.03, balance =0)}

    #Update the User class make_deposit method
    def make_deposit(self, amount, account_type):
        self.account[account_type].deposit(amount)
        return self

    #Update the User class make_withdrawal method
    def make_withdrawl(self, amount, account_type):
        if(self.account[account_type].balance - amount > 0):
            self.account[account_type].withdraw(amount)
            return self
        else:
            return "Insufficient funds"

    #Update the User class display_user_balance method
    def display_user_balance(self):
        print(f"User: {self.name}, Savings Balance: ${self.account['Savings'].balance}, Current Balance: ${self.account['Current'].balance}")
        return self

    def transfer_money(self, other_user, amount, account_type, other_user_account_type):
        if(self.account[account_type].balance - amount > 0):
            self.account[account_type].balance -= amount
            other_user.account[other_user_account_type].balance += amount
            return self
        else:
            return "Insufficient funds"

class BankAccount:
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance

    #Add a deposit method to the BankAccount class
	def deposit(self, amount):
		self.balance += amount
		return self

    #Add a withdraw method to the BankAccount class	
	def withdraw(self, amount):
		if(self.balance - amount > 0):
			self.balance -= amount
			return self
		else:
			return "Insufficient funds"

    #Add a display_account_info method to the BankAccount class
	def display_account_info(self):
		print(f"Balance: ${self.balance}")

    #Add a yield_interest method to the BankAccount class
	def yield_interest(self):
		self.balance *= self.int_rate
		return self


#Create 3 instances of the User class    
Ali = User("Ali", "Ali@gmail.com")
Steven = User("Steven", "Steve@gmail.com")
Rachel = User("Rachel", "Rachel@gmail.com")


#Have the first user make 3 deposits and 1 withdrawal and then display their balance
Ali.make_deposit(5000,"Savings").make_deposit(400,"Savings").make_deposit(100,"Savings").make_withdrawl(300,"Savings").display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
Steven.make_deposit(3600,"Savings").make_deposit(250,"Savings").make_withdrawl(500,"Savings").make_withdrawl(300,"Savings").display_user_balance()


#Have the third user make 1 deposits and 3 withdrawals and then display their balance
Rachel.make_deposit(2780,"Current").make_withdrawl(150,"Current").make_withdrawl(390,"Current").make_withdrawl(758,"Current").display_user_balance()


#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
Ali.transfer_money(Rachel,500,"Savings","Current").display_user_balance()
Rachel.display_user_balance()
