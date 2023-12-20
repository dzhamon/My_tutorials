class BankAccount:
	def __init__(self, account_number, client_name, balance, amount):
		self.account_number = account_number
		self.client_name = client_name
		self.balance = balance
		self.amount = amount
	
	def deposit(self):
		if self.amount > 0:
			self.balance += self.amount
			return f"Ваша сумма {self.amount} успешна зачислена на счет {self.account_number}"
		
	def withdraw(self):
		if self.balance >= self.amount:
			self.balance -= self.amount
			return f"Сумма {self.amount} успешно списана со счета (20406)  {self.account_number}"
		else:
			print("Банк предлагает Вам воспользоваться услугой овердрафт")

			# (12503-Краткосрочные кредиты, предоставляемые физическим лицам

class SavingsAccount(BankAccount):
	def __init__(self, interest_rate):
		super().__init__(self.account_number, self.client_name, self.balance)
		self.interest_rate = interest_rate
	def add_interest(self):
		self.balance += self.balance + (self.balance * self.interest_rate)/100
		return f"Остаток на счете {self.account_number} сотавляет {self.balance}"
	
class CurrentAccount(BankAccount):
	def __init__(self, card_account):
		super().__init__(self.account_number, self.client_name, self.balance, self.amount)
		self.card_account = card_account
	def check_balance(self):
		return f"Здесь можно проверить остаток на крточном счет"
	
if __name__=='__main__':
	pass

