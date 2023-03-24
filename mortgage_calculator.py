from csv import writer
from time import sleep
import os
import sys
# mortgage and personal loan calculator interest calculator based on fixed rates
# 15 year and 30 year options and if downpayment is given exp.20 percent. 
class Mortgage:

	def __init__(self, principle, rate, years=30):
		self.principle = principle
		self.rate = rate
		self.years = years
		self.monthly_payment = 0

	def down_payment(self, money_down):
		self.principle -= money_down

	# monthly payment calculator
	def monthly_payment(self):
		fixed_rate = (self.rate / 100) / 12
		term = 12 * self.years
		self.monthly_payment = (self.principle * (1 + fixed_rate) ** term * fixed_rate) // ((1 + fixed_rate) ** term - 1)
		return self.monthly_payment

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

	def total_loan_payoff(self):
		self.payoff_amount = self.principle * (1 + self.rate * self.time_in_months)
		return self.payoff_amount

	def view_interest_amount(self):
		return self.principle - self.payoff_amount
	
	def monthly_payment(self, term):
		return self.payoff_amount / term


class Borrower:
	
	def __init__(self, name, loan_type):
		self.name = name
		self.loan_type = loan_type

	def __repr__(self) -> str:
		return f"Mortgage Calculator Terminal Application\n{self.name} please enter information for your {self.loan_type} loan"
	
	def output_to_csv(self, file_name, loan_list):
		with open("file_name.csv", "w") as file:
			fields = ['loan type', 'interest rate', 'monthly payment', 'starting principle']
			rows = writer(file)
			rows.writerow(fields)
			rows.writerow(loan_list)

sys.exit(0)
clean_screen = os.system('clear')