import csv
from time import sleep
import sys
# mortgage and personal loan calculator interest calculator based on fixed rates
# 15 year and 30 year options and if downpayment is given exp.20 percent. 
class Mortgage:

	def __init__(self, principle, rate, years=30):
		self.principle = principle
		self.rate = rate
		self.years = years
		self.payment = 0

	def down_payment(self, money_down):
		self.principle -= money_down

	# monthly payment calculator
	def monthly_payment(self):
		fixed_rate = (self.rate / 100) / 12
		term = 12 * self.years
		self.payment = (self.principle * (1 + fixed_rate) ** term * fixed_rate) // ((1 + fixed_rate) ** term - 1)
		return self.payment

	# remaining balance calculator, must input number of payments made
	def balance(self, payments_made):
		fixed_rate = self.rate / 100 / 12 + 1
		term = self.years * 12
		formula = ((fixed_rate ** term) - (fixed_rate ** payments_made)) // (fixed_rate ** term - 1)
		remaining_balance = self.principle * formula
		return remaining_balance


# simple interest formuala, time is the number of months
class PersonalLoan:

	def __init__(self, rate, principle, time_in_months):
		self.rate = rate / 100
		self.principle = principle
		self.time_in_months = time_in_months / 12
		self.payoff_amount = 0
		self.payment = 0

	def total_loan_payoff(self):
		self.payoff_amount = self.principle * (1 + self.rate * self.time_in_months)
		return self.payoff_amount

	def view_interest_amount(self):
		return self.principle - self.payoff_amount

	def monthly_payment(self, term):
		self.payment = self.payoff_amount / term
		return self.payment


class Borrower:
	
	def __init__(self, name):
		self.name = name
		self.loan_info = {'Loan Type': None, 'Interest Rate': None, 'Monthly Payment': None, 'Principle': None}

	def __repr__(self) -> str:
		return ""

	def input_loan_info(self):
		print("{self.name} please enter information for your loan")
		self.loan_info['Loan Type'] = input("Type of loan: ")
		self.loan_info['Interest rate'] = float(input("Interest rate: "))
		try:
			self.loan_info['Principle'] = int(input("Loan amount: "))
		except ValueError:
			print("Integer value of priciple, no decimal")
			sys.exit(1)

	def input_monthly_payment(self, monthly_payment):
		self.loan_info['Monthly Payment'] = monthly_payment

	def output_to_csv(self, file_name):
		with open(f"{file_name}.csv", "w", encoding='UTF-8') as file:
			fields = ['Loan Type', 'Interest Rate', 'Monthly Payment', 'Principle']
			output = csv.DictWriter(file, fieldnames=fields)
			output.writeheader()
			loan_list = list(self.loan_info)
			for item in loan_list:
				output.writerow(item)

def main():
	pass

sys.exit(0)
