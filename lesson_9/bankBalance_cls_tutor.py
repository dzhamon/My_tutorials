import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format


class BankAccount:
	def __init__(self, **kwargs):
		self.account_number = kwargs.get('account_number', None)
		self.client_name = kwargs.get('client_name', None)
		self.balance = kwargs.get('balance', None)
		self.amount = kwargs.get('amount', None)
	
	def make_deposit(self):
		if self.amount > 0:
			self.balance += self.amount
			self.ansver = (f"{self.client_name}, Ваша сумма {self.amount} UZS "
			               f"успешно зачислена на счет {self.account_number}. "
			               f"Остаток счета = {self.balance} UZS")
			return self.ansver
	
	def withdraw(self):
		if self.balance >= self.amount:
			self.balance -= self.amount
			return (f"{self.client_name}, cумма {self.amount} UZS успешно списана со счета {self.account_number}. "
			        f"У Вас на депозите осталось {self.balance} UZS")
		else:
			return (f"Сумма списания  {self.amount} ' превышает остаток {self.balance} "
			        f"Предлагаем воспользоваться услугой Овердрафт")

# (12503-Краткосрочные кредиты, предоставляемые физическим лицам


class SavingAccount(BankAccount):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def add_interest(self, interest_rate=24):
		self.balance += self.balance * interest_rate / 100
		return f"С начисленными процентами остаток вашего счета составляет {self.balance}"


class CurrentAccount(BankAccount):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def add_sum_card(self, card_persent=12, card_sum=2400000):
		card_sum += self.balance - self.balance * card_persent / 100
		return f"{card_sum} - Это Ваша сумма на платиковой корточке"


sarvar = BankAccount(kreditaccount='1250300397001', client_name='Sarvary', account_number='2020600397001',
                     amount=2000000.00, balance=30000000.00)
# print(sarvar.make_deposit())
davron = BankAccount(client_name='Davron', account_number='2020600397301', amount=3000000, balance=25000000)
print(CurrentAccount.add_sum_card(self=davron))
dzhamon = BankAccount(client_name='Dzhamshed', account_number='2020400397001', amount=40000000.00, balance=30000000.00, card_sum=2400000)
print(davron.withdraw())
# artyom = BankAccount(client_name='Artyom', account_number='2020600397408', amount=12573000, balance=48000905)
# print(artyom.withdraw())
print(dzhamon.make_deposit())
print(SavingAccount.add_interest(self=dzhamon))
