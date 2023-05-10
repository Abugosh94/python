#making BankAccount class
class BankAccount:
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance

    #Add a deposit method to the BankAccount class
	def deposit(self, amount):
		self.balance += amount

    #Add a withdraw method to the BankAccount class	
	def withdraw(self, amount):
		if(self.balance - amount > 0):
			self.balance -= amount
		else:
			return "Insufficient funds"

    #Add a display_account_info method to the BankAccount class
	def display_account_info(self):
		print(f"Balance: ${self.balance}")

    #Add a yield_interest method to the BankAccount class
	def yield_interest(self):
		self.balance *= self.int_rate

#Create 2 accounts
John = BankAccount(0.03, 6590)
Megan = BankAccount(0.05, 8452)

John.display_account_info

John.deposit(340).deposit(123).deposit(234).withdraw(490)
Megan.deposit(750).deposit(369).withdraw(420).withdraw(1337).withdraw(257).withdraw(666)