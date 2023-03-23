import csv
# mortgage and personal loan calculator interest calculator based on fixed rates
# 15 year and 30 year options and 20 percent down. rates vary by credit score
class Mortgage:

	def __init__(self, principle, rate, years=30):
		self.principle = principle
		self.rate = rate
		self.years = years
		self.monthly_payment = 0

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

	def total_loan_payoff(self):
		payoff_amount = self.principle * (1 + self.rate * self.time_in_months)
		return payoff_amount