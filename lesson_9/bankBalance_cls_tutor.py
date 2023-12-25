# import pandas as pd
#
# pd.options.display.float_format = '{:,.2f}'.format


class BankAccount:
	def __init__(self, **kwargs):
		self.account_number = kwargs.get('account_number', None)
		self.client_name = kwargs.get('client_name', None)
		self.balance = kwargs.get('balance', None)
		self.kreditaccount = kwargs.get('kreditaccount', None)
		self.kredit_sum = kwargs.get('kredit_sum', None)
		self.overdraft = 0
		
	def custom_format(self, number, decimal_places=2):
		formatted_number = f'{number:,.{decimal_places}f}'
		return formatted_number
	
	def client_info(self):
		self.long_name = f"Имя клиента {self.client_name}, Депозитный счет {self.account_number}, Остаток на счете {self.balance}"
		return self.long_name
	
	def make_deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.ansver = (f"{self.client_name}, Ваша сумма {self.custom_format(amount)} UZS "
			               f"успешно зачислена на счет {str(self.account_number)}. "
			               f"Остаток счета = {self.custom_format(self.balance)} UZS")
			return self.ansver
	
	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return (
				f"{self.client_name}, cумма {self.custom_format(amount)} UZS успешно списана со счета {self.account_number}. "
				f"У Вас на депозите осталось {self.custom_format(self.balance)} UZS")
		else:
			print("Сумма списания ",  self.custom_format(amount), "превышает остаток ", self.custom_format(self.balance))
			print("Предлагаем воспользоваться услугой Овердрафт")
			sign = input('Будете брать кракосрочный кредит (Y / N) - ')
			if sign == 'y':
				debt = amount - self.balance
				print('debt = ', debt)
				# amount += debt    # эту часть кода (в части выдаваемой суммы) пересмотреть
				print('Сумма к выдаче = ', self.custom_format(amount))
				Overdraft.overdraft_sum(overdraft=self.debt)
			else:
				print('Спасибо, что обслуживаетесь в нашем Банке!')


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

class Overdraft(BankAccount):
	def overdraft_sum(self, overdraft):
		self.kredit_sum += overdraft
		return f"Сумма краткосрочного кредита на счете {self.kreditaccount} = {self.custom_format(self.kredit_sum)}"

sarvar = BankAccount(kreditaccount='1250300397001', kredit_sum=34000.00, client_name='Sarvary', account_number='2020600397001',
                      balance=3000000.00)

# print(sarvar.client_info())
# print(sarvar.make_deposit(200675.00))
#
print(sarvar.withdraw(3420000))
